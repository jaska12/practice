/**
 * E-TASK: Bitta string argumentni qabul qilib,
 * o'sha stringni teskari qilib return qiladigan funksiya.
 * * MASALAN: getReverse("hello") => "olleh"
 */

function getReverse(text) {
    // 1. split('') - matnni har bir harfini alohida element qilib massivga aylantiradi
    // 2. reverse() - massiv elementlarini teskari tartibga o'giradi
    // 3. join('') - massiv elementlarini yana bitta matnga birlashtiradi
    return text.split('').reverse().join('');
}

// --- TEKSHIRISH ---

// 1
const result1 = getReverse("hello");
console.log("Natija 1:", result1);

// 2
const result2 = getReverse("mitgroup");
console.log("Natija 2:", result2);

// 3
const result3 = getReverse("futureengineer");
console.log("Natija 3:", result3);






/**
 * C-TASK (NodeJS)
 * * Shunday function tuzing, u 2ta string parametrga ega bolsin.
 * Agar har ikkala string bir xil harflardan iborat bolsa true,
 * aks holda false qaytarsin.
 * * MASALAN: checkContent("futureengineer", "engineerfuture") return true

function checkContent(word1, word2) {
    // 1. Uzunlikni tekshirish
    if (word1.length !== word2.length) {
        return false;
    }

    // 2. Harflarni kichik qilib, word2 ni massivga o'tkazamiz
    let arr2 = word2.toLowerCase().split('');
    let str1 = word1.toLowerCase();

    // 3. For loop yordamida word1 dagi har bir harfni aylanib chiqamiz
    for (let i = 0; i < str1.length; i++) {
        let char = str1[i];

        // indexOf harfning ikkinchi massivdagi o'rnini (index) topadi
        let index = arr2.indexOf(char);

        // 4. Agar harf topilsa, uni massivdan o'chirib tashlaymiz
        if (index !== -1) {
            arr2.splice(index, 1);
        } else {
            return false;
        }
    }

    return arr2.length === 0;
}

// --- TEKSHIRISH ---

// Musbat holat (Haqiqatdan bir xil harflar)
const result1 = checkContent("futureengineer", "engineerfuture");
console.log("Natija 1:", result1); // true

// Manfiy holat (Uzunlik bir xil, lekin bitta harf boshqa)
const result2 = checkContent("futureengineer", "futureengineee");
console.log("Natija 2:", result2); // false

*/


/*
B-TASK:
Shunday function tuzing, u 1ta string parametrga ega bolsin,
hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.

MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/


//  Masalaning yechimi:
/*function countDigits(text) {
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
console.log("Digits count:", result);*/

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

