/* A-TASK:
Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi 
letterni ikkinchi parametrdagi so'zdan qatnashgan sonini return qilishi kerak bo'ladi.
MASALAN: countLetter("e", "engineer") 3ni return qiladi.
*/

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

// "Full Stack Developer" so'zida nechta 'l' harfi borligini tekshiramiz
const res = countLetter("l", "Full Stack Developer");
console.log(res);

const res2 = countLetter("e", "Full Stack Developer");
console.log(res2); 
