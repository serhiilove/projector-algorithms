# a. for (i = n; i > 1; i /= 2)
#  		db_call()
#
# підходить, зробимо порядку n/2 викликів, що меньше n^n


# b. for (i = 0; i * i < n; i++)
# 		db_call()
#
# підходить, зробимо порядку n^2 викликів, що меньше n^n


# c. for (i = 0; i < n; i++)
# 	  	for (j = 0; j < 356; j++)
# 		  db_call()
#
# підходить, сладність лінійна, зробимо порядку n * 356 викликів, що меньше n^n


# d. for (i = 1; i <= n * n - 10; i++)
# 		for (j = 1; j <= i; j ++)
# 			db_call()
#
# не підходить, складність експоненційна, зробимо порядку n^3 / 2 викликів

# e.  for (i = 1; i <= n; i++)
# 		for (j = 1; j <= i; j++)
# 			for (k = 1; k <= j; k++)
# 				db_call()
#
# f. for (i = 1; i <= n; i++)
# 		for (j = 1; j < i; j *= 2)
# 			db_call()
#
# g. for (i = 1; i <= n; i++)
# 		for (j = 1; j <= n; j += i)
# 			db_call()
#
# h. void compute(int n)
# 	  if (n == 0) return;
# 	  for (int i = 0; i < n; i++)
# 	  	  db_call()
# 	  compute(n/2)
# 	  compute(n/2)


