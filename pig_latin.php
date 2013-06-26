<?php

function pig_latinize($raw_word) {
    /*
     *  Return a pig latin-ized version of a word
     */
    $VOWELS = array("a","e","i","o","u","y");
    $word = strtolower($raw_word);
    // check for the first vowel
    $index = 0;
    foreach(str_split($word) as $letter) {
        if(in_array($letter, $VOWELS)) {
            if($index > 0) {
                // first letter is not a vowel
                return substr($word, $index, strlen($word)) . substr($word, 0, $index) . "ay";
            } else {
                // first letter is a vowel
                return $word . "yay";
            }
        }
        $index++;
    }
    # no vowels... let's just add an "ay"
    return $word . "ay";
}

assert('pig_latinize("happy") == "appyhay"');
assert('pig_latinize("duck") == "uckday"');
assert('pig_latinize("egg") == "eggyay"');
assert('pig_latinize("thbbbt") == "thbbbtay"');

?>