#!/bin/bash

echo "🔧 MongoDB Connection String Updater"
echo ""
echo "Please enter your MongoDB Atlas connection string:"
echo "Format: mongodb+srv://username:password@cluster.mongodb.net/database"
echo ""
read -p "MongoDB URI: " mongodb_uri

if [ -z "$mongodb_uri" ]; then
    echo "❌ No connection string provided. Exiting."
    exit 1
fi

# Add connection options if not present
if [[ ! "$mongodb_uri" == *"?"* ]]; then
    mongodb_uri="${mongodb_uri}?retryWrites=true&w=majority"
fi

# Update .env file
cd shield360-backend
if [ -f ".env" ]; then
    # Backup existing .env
    cp .env .env.backup
    echo "✅ Backed up existing .env to .env.backup"
    
    # Update MONGODB_URI
    if grep -q "MONGODB_URI=" .env; then
        # Use sed to replace the line (works on Linux/Mac)
        sed -i.bak "s|MONGODB_URI=.*|MONGODB_URI=$mongodb_uri|" .env
        rm .env.bak 2>/dev/null
    else
        echo "MONGODB_URI=$mongodb_uri" >> .env
    fi
    
    echo "✅ Updated MongoDB URI in .env file"
    echo ""
    echo "Testing connection..."
    npm run check-db
else
    echo "❌ .env file not found. Creating new one..."
    cat > .env << EOF
PORT=5000
MONGODB_URI=$mongodb_uri
JWT_SECRET=shield360_secret_key_change_in_production
NODE_ENV=development
EOF
    echo "✅ Created .env file with MongoDB URI"
    echo ""
    echo "Testing connection..."
    npm run check-db
fi


