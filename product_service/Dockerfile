FROM php:7.3.6-fpm-alpine3.9
RUN apk add --no-cache openssl bash mysql-client nodejs npm alpine-sdk autoconf librdkafka-dev vim nginx openrc
RUN mkdir -p /run/nginx && \
    echo "pid /run/nginx.pid;" >> /etc/nginx/nginx.conf

RUN docker-php-ext-install pdo pdo_mysql bcmath


WORKDIR /var/www

RUN rm -rf /var/www/html
RUN ln -s public html

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN rm /etc/nginx/conf.d/default.conf
COPY .docker/nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 9000

ENTRYPOINT [ "php-fpm" ]