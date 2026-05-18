/**
 * N-TASK: 
 * Shart: Shunday function yozing, u raqamlardan tashkil topgan array 
 * qabul qilsin va array ichidagi har bir raqam uchun raqamni o'zi 
 * hamda o'sha raqamni kvadratidan tashkil topgan object hosil qilib, 
 * hosil bo'lgan objectlarni array ichida qaytarsin.
 * 
 * MASALAN: getSquareNumbers([1, 2, 3]) return 
 * [{number: 1, square: 1}, {number: 2, square: 4}, {number: 3, square: 9}];
 */

function getSquareNumbers(arr) {
    // 1. .map() metodi orqali array ichidagi har bir raqamni aylanib chiqamiz
    const result = arr.map((num) => {
        // 2. Har bir raqam uchun yangi obyekt hosil qilib qaytaramiz
        return {
            number: num,
            square: num * num // Raqamning kvadrati
        };
    });

    // 3. Hosil bo'lgan obyektlar massivini qaytaramiz
    return result;
}

// --- TEKSHIRISH ---

// 1. Misoldagi ketma-ket sonlar holati
const result1 = getSquareNumbers([1, 2, 3]);
console.log("result 1:", result1);

// 2. Turli xil sonlar berilgan holat
const result2 = getSquareNumbers([4, 7, 10]);
console.log("result 2:", result2);


/**
 * L-TASK:
 * Shart: Shunday function yozing, u string qabul qilsin va
 * string ichidagi hamma so'zlarni chappasiga yozib va
 * so'zlar ketma-ketligini buzmasdan stringni qaytarsin.
 *
 * MASALAN: reverseSentence("we like coding!") return "ew ekil !gnidoc"


function reverseSentence(sentence) {
    // 1. Gapni so'zlarga ajratib olamiz (bo'sh joy orqali)
    const words = sentence.split(' ');

    // 2. Har bir so'zni alohida chappasiga o'girib chiqamiz
    const reversedWords = words.map((word) => {
        // So'zni harflarga ajratamiz, teskari qilamiz va qayta birlashtiramiz
        return word.split('').reverse().join('');
    });

    // 3. Teskari o'girilgan so'zlarni qaytadan gap ko'rinishida birlashtiramiz
    return reversedWords.join(' ');
}

// --- TEKSHIRISH ---

// 1. Misoldagi holat
const result1 = reverseSentence("we like coding!");
console.log("result 1:", result1); // "ew ekil !gnidoc"

// 2. Boshqa bir gap bilan tekshirish
const result2 = reverseSentence("Javascript is awesome");
console.log("result 2:", result2); // "tpircsavaJ si emosewa"

// 3. Bitta so'zli holat
const result3 = reverseSentence("Hello");
console.log("result 3:", result3); // "olleH"
*/
/**
 * J-TASK:
 * Shart: Shunday function yozing, u parametridagi array ichida
 * eng ko'p takrorlangan raqamni topib qaytarsin.
 *
 * MASALAN: majorityElement([1, 2, 3, 4, 5, 4, 3, 4]) return 4


function majorityElement(arr) {
    const countMap = {};
    let maxCount = 0;
    let mostFrequent = arr[0];

    // 1. Har bir raqamning necha marta takrorlanganini hisoblab chiqamiz
    for (const num of arr) {
        // Agar raqam obyektda bo'lsa +1, bo'lmasa 1 deb belgilaymiz
        countMap[num] = (countMap[num] || 0) + 1;

        // 2. Hisoblash jarayonida eng katta takrorlanishni aniqlab boramiz
        if (countMap[num] > maxCount) {
            maxCount = countMap[num];
            mostFrequent = num;
        }
    }

    return mostFrequent;
}

// --- TEKSHIRISH ---

// 1. Misoldagi holat (4 raqami 3 marta takrorlangan)
const result1 = majorityElement([1, 2, 3, 4, 5, 4, 3, 4]);
console.log("result 1:", result1); // 4

// 2. Boshqa bir holat (10 raqami eng ko'p)
const result2 = majorityElement([10, 20, 10, 5, 10, 30]);
console.log("result 2:", result2); // 10

// 3. Bir xil miqdorda takrorlanish bo'lsa, birinchisini qaytaradi
const result3 = majorityElement([1, 1, 2, 2]);
console.log("result 3:", result3); // 1

*/

/**
 * H-TASK:
 * Shart: Shunday function tuzing, u integerlardan iborat arrayni
 * argument sifatida qabul qilib, faqat positive (musbat)
 * qiymatlarni olib string holatda return qilsin.
 *
 * MASALAN: getPositive([1, -4, 2]) return qiladi "12"


function getPositive(arr) {
    // 1. Array ichidan filter metodi yordamida faqat 0 dan katta sonlarni ajratib olamiz
    const positives = arr.filter((num) => num > 0);

    // 2. Hosil bo'lgan musbat sonlar massivini join('') orqali bitta matn (string) holatiga keltiramiz
    return positives.join('');
}

// --- TEKSHIRISH ---

// 1. Aralash sonlar berilgan holat
const result1 = getPositive([1, -4, 2]);
console.log("result 1:", result1); // "12"

// 2. Katta va turli xil musbat sonlar qatnashgan holat
const result2 = getPositive([-5, 10, -3, 20]);
console.log("result 2:", result2); // "1020"

// 3. Faqat manfiy sonlar berilgan holat
const result3 = getPositive([-1, -2, -3]);
console.log("result 3:", result3); // "" (bo'sh string qaytadi)

*/

/**
 * F-TASK: Bitta string argumentni qabul qilib,
 * agar stringda bir xil harf qatnashgan bo'lsa true,
 * qatnashmasa false qaytaradigan funksiya.
 * * MASALAN: findDoublers("hello") => true


function findDoublers(text) {
    // 1. split('')
    const letters = text.split('');
    //2/ Bu yerda har bir harfning massivdagi birinchi va oxirgi indeksi mos kelmasligini tekshiramiz
    return letters.some((char, index) => letters.indexOf(char) !== index);
}

// --- TEKSHIRISH ---

// 1. Takrorlanuvchi harf bor holat (l harfi)
const result1 = findDoublers("hello");
console.log("result 1:", result1); // true

// 2. Takrorlanuvchi harf yo'q holat
const result2 = findDoublers("mitgroup");
console.log("result 2:", result2); // false

// 3. Takrorlanuvchi harf bor holat (e harfi)
const result3 = findDoublers("futureengineer");
console.log("result 3:", result3); // true
*/


/**
 * E-TASK: Bitta string argumentni qabul qilib,
 * o'sha stringni teskari qilib return qiladigan funksiya.
 * * MASALAN: getReverse("hello") => "olleh"


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
*/





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

