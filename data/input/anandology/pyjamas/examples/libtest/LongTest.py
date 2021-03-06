from UnitTest import UnitTest

class LongTest(UnitTest):

    def testAdd(self):
        x = 0L
        y = 1L
        x += y
        self.assertTrue(x == 1L)

    def testType(self):

        # int shifted up ends up as a long
        x = 1<<64
        self.assertTrue(x == 18446744073709551616L, "#302 - %s != 18446744073709551616L" % repr(x))
        self.assertTrue(isinstance(x, long))

        # long shifted up is still a long
        x = 1L<<64
        self.assertTrue(x == 18446744073709551616L, "%s != 18446744073709551616L" % repr(x))
        self.assertTrue(isinstance(x, long))

        x = 1<<20
        self.assertTrue(x == 1048576, "%s != 1048576" % repr(x))
        self.assertTrue(isinstance(x, int))

        x = 1L<<20
        self.assertTrue(x == 1048576L, "%s != 1048576L" % repr(x))
        self.assertTrue(isinstance(x, long))

        self.assertTrue(int(18446744073709551616) is 18446744073709551616L, "No automatic int to long conversion")

        if int(18446744073709551616) == 18446744073709551616L:
            # We do have long type

            x = 1<<64
            self.assertEqual(x, 18446744073709551616L)

            x = 0x7fffffff + 1
            self.assertEqual(x, 2147483648L)

            x = 0x7fffffff + 0x7fffffff
            self.assertEqual(x, 4294967294L)

            x = -0x7fffffff - 2
            self.assertEqual(x, -2147483649L)

            x = -0x7fffffff - 0x7fffffff
            self.assertEqual(x, -4294967294)

            x = 0x7fffffff * 2
            self.assertEqual(x, 4294967294)

            x = 0x7fffffff * -2
            self.assertEqual(x, -4294967294)

            x = 0x7ffff ** 2
            self.assertEqual(x, 274876858369)

            self.assertEqual(1 << 2L, 4L)
            self.assertEqual(6 >> 2L, 1L)

            x = 1
            x <<= 3L
            self.assertEqual(x, 8L)
            x = 8
            x >>= 1L
            self.assertEqual(x, 4L)

