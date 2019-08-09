<?php

function test($x)
{
    $t1 = microtime(true);
    $a = 0;
    for($i = 0; $i < $x; $i++)
    {
        $a++;
    }
    $t2 = microtime(true);

    echo "Time for $x was " . ($t2 - $t1) . "\n";

    return $a;
}


echo test(10000000000);
?>
