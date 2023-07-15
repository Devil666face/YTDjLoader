server {
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name yt.devilface.ru;
	#location /static/ {
	#	root /var/www/YTDjLoader;
	#}
	location /media/ {
		root /var/www/YTDjLoader;
	}
	location / {
		proxy_pass http://127.0.0.1:8002;
		proxy_set_header Host $host;
		proxy_set_header X-Forwarded-Host $server_name;
		proxy_set_header X-Real-IP $remote_addr;
		add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
		add_header Access-Control-Allow_Origin *;
	}
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/yt.devilface.ru/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yt.devilface.ru/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

}
server {
    if ($host = yt.devilface.ru) {
        return 301 https://$host$request_uri;
    }
	server_name yt.devilface.ru;
    listen 80;
    return 404;
}
