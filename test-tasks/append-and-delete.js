'use strict';

function appendAndDelete(s, t, k) {
    let commonLength = 0;

    for (let i = 0; i < Math.min(s.length, t.length); i++) {
        if (s.charAt(i) === t.charAt(i)) {
            commonLength++;
        }  else break;
    }

    const minK = s.length + t.length -2*commonLength;

    if (minK > k) return 'No';

    if (k >= s.length + t.length) return 'Yes';

    if ((k - minK) % 2 === 0) return 'Yes';

    return 'No'
}

const result = appendAndDelete('ashley', 'ash', 2);
console.log(result);