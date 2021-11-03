//A.
//Speedup random image processing
//
//const int N = 4096;
//byte [,] image = new byte[N, N];
//public bool isDark() {
//    count = 0
//    for (int j = 0; j < N; ++j) {
//        for (int i = 0; i < N; ++i) {
//             if (image[i, j] >= 128) {
//                count += 1;
//            }
//        }
//   }
//
//   return count < N * N / 2;
//}

// solution A-1
const int N = 4096;
byte [,] image = new byte[N, N];
public bool isDark() {
    count = 0
    half = N * (N / 2) // меньше число поділиться швидше
    for (int j = 0; j < N; ++j) {
        for (int i = 0; i < N; ++i) {
            count += 1 * (image[i, j] >= 128)
        }
        if (count > half) {
            return false // завершити раніше, якщо більше половити комірок світлі
        }
   }
   return count < half;
}

// solution A-2
const int N = 4096;
byte [,] image = new byte[N, N];
public bool isDark() {
    count = 0
    for (int j = 0; j < N; ++j) {
        for (int i = 0; i < N; ++i) {
            count += 1 * (image[i, j] >= 128) // avoid JGE assembly instructions
        }
   }
   return count < N * (N / 2);
}

