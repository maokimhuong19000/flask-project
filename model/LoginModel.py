from config.configdb import PgConfig, con
import random


class LoginDto:
    __uname = None
    __upass = None
    __confirm_code = None

    @property
    def UName(self):
        return self.__uname

    @UName.setter
    def UName(self, value):
        self.__uname = value

    @property
    def UPass(self):
        return self.__upass

    @UPass.setter
    def UPass(self, value):
        self.__upass = value

    @property
    def ConfirmCode(self):
        return self.__confirm_code

    @ConfirmCode.setter
    def ConfirmCode(self, value):
        self.__confirm_code = value


class LoginDao:
    def verify_auth(self, logindto):
        cur = PgConfig.getCursor()
        try:
            cur.execute("SELECT * FROM public.tbluser WHERE is_active=true and uname=%s and upass=%s", (logindto.UName, logindto.UPass))
            if cur.rowcount > 0:
                # Assuming you're storing hashed passwords, you should validate the password here
                # e.g., using bcrypt or another hashing library
                # if not bcrypt.checkpw(logindto.UPass.encode('utf-8'), stored_hashed_password):
                #     return False

                # Generate a confirmation code
                val = random.randrange(100000, 999999)
                cur.execute(
                    "UPDATE public.tbluser SET confirm_code=%s, code_exp=now()+'2 minutes'::interval WHERE is_active=true AND uname=%s",
                    (str(val), logindto.UName)
                )
                PgConfig.PgCommit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Database error: {e}")
            con.rollback()  # Roll back the transaction on error
            return False

    def confirm_code(self, logindto):
        cur = PgConfig.getCursor()
        try:
            cur.execute(
                "SELECT * FROM public.tbluser WHERE is_active=true AND uname=%s AND confirm_code=%s AND now()<=code_exp",
                (logindto.UName, logindto.ConfirmCode))
            return cur.rowcount > 0
        except Exception as e:
            print(f"Database error: {e}")
            con.rollback()  # Roll back the transaction on error
            return False
