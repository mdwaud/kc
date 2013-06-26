<?php

define('LETTER_LIMIT', 3);

function pig_latinize($word) {
    /*
     *  Return a pig latin-ized version of a word
     */
    $VOWELS = array("A","E","I","O","U",);
    $IGNORE_LIST = array("THE",);
    // check some simple base cases
    if (strlen($word) < LETTER_LIMIT || in_array(strtoupper($word), $IGNORE_LIST)) {
        return $word;
    }
    // check for the first vowel
    $index = 0;
    foreach(str_split($word) as $letter) {
        if(in_array(strtoupper($letter), $VOWELS)) {
            return substr($word, $index, strlen($word)) . substr($word, 0, $index) . "ay";
        }
        $index++;
    }
    # no vowels, so just return what we got
    return $word;
}

assert('pig_latinize("Computer") == "omputerCay"');
assert('pig_latinize("Crevice") == "eviceCray"');
assert('pig_latinize("My") == "My"');
assert('pig_latinize("the") == "the"');
assert('pig_latinize("amber") == "amberay"');

?>