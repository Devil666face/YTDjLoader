#!/bin/bash
read -p "Create systemd unit? [y/n] " STATUS
if [[ "$STATUS" = "y" ]]; then
	sed -i 's|%PWD%|'"$PWD"'|g' ./ytdjloader.service
	ln -s $PWD/ytdjloader.service /etc/systemd/system/ytdjloader.service
	systemctl daemon-reload
	systemctl enable ytdjloader.service --now
fi
read -p "Create .env file? [y/n] " STATUS
if [[ "$STATUS" = "y" ]]; then
	read -p "HOST" HOST
	read -p "PORT" PORT
	read -p "SECRET_KEY" SECRET_KEY
	read -p "ALLOWED_HOSTS" ALLOWED_HOSTS
	read -p "DEBUG" DEBUG
	read -p "CSRF_COOKIE_DOMAIN" CSRF_COOKIE_DOMAIN
	read -p "CSRF_TRUSTED_ORIGINS" CSRF_TRUSTED_ORIGINS
	echo "HOST=$HOST" >> .env
	echo "PORT=$PORT" >> .env
	echo "SECRET_KEY=$SECRET_KEY" >> .env
	echo "ALLOWED_HOSTS=$ALLOWED_HOSTS" >> .env
	echo "DEBUG=$DEBUG" >> .env
	echo "CSRF_COOKIE_DOMAIN=$CSRF_COOKIE_DOMAIN" >> .env
	echo "CSRF_TRUSTED_ORIGINS=$CSRF_TRUSTED_ORIGINS" >> .env
fi
chown -R www-data:www-data ../YTDjLoader
