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
    return (((m % n) + (s - 1)) % n) || n;
}

const result = saveThePrisoner(3, 5, 3);
console.log(result);
