import java.lang.invoke.MethodHandle;
import java.lang.invoke.MethodHandles;
import java.lang.invoke.MethodType;

public class Main {
        public static class BadCast1 extends Throwable{
                Object o1 = MethodHandles.publicLookup();
        }

        public static class BadCast2 extends Throwable{
                LookupMirror lm = new LookupMirror();
        }

        public static void throwEx() throws BadCast1{
                throw new BadCast1();
        }

