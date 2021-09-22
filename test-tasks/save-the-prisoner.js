'use strict';

/**
 * Save the prisoner
 * @param n - prisoners
 * @param m - candies
 * @param s - start position
 * @returns {number} - last candy position
 * @type {(n : number, m : number, s : number) => number}
 */

function saveThePrisoner (n, m, s) {
    if (m % n === 0) return s - 1 < 1 ? n : s - 1;

    const leftPrisoners = n - s + 1;

    const leftCandies = Math.trunc(m / n) > 0 ? m % n : m;

    return leftCandies > leftPrisoners ? leftCandies - leftPrisoners : s + leftCandies - 1;
}

const result = saveThePrisoner(1, 1, 1);
console.log(result);
