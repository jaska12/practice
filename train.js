/* A-TASK:
Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi 
letterni ikkinchi parametrdagi so'zdan qatnashgan sonini return qilishi kerak bo'ladi.
MASALAN: countLetter("e", "engineer") 3ni return qiladi.


//  Masalaning yechimi:
function countLetter(letter, word) {
    let count = 0;

    // Matndagi har bir harfni tekshiramiz
    for (let i = 0; i < word.length; i++) {
        // word[i] - bu matndagi har bir harf (F, u, l, l...)
        if (word[i].toLowerCase() === letter.toLowerCase()) {
            count++;
        }
    }

    return count;
}
*/

/*
B-TASK:
Shunday function tuzing, u 1ta string parametrga ega bolsin, 
hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.

MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/


//  Masalaning yechimi:
function countDigits(text) {
    let count = 0;

    for (let i = 0; i < text.length; i++) {
        // Char raqam ekanligini tekshirish (bo'shliq bo'lmasligi va raqam bo'lishi sharti)
        if (text[i] >= '0' && text[i] <= '9') {
            count++;
        }
    }

    return count;
}

const result = countDigits("ad2a54y79wet0sfgb9");
console.log("Digits count:", result);