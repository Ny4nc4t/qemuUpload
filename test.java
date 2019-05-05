class Cast1 extends Throwable { 
	Object Lemon;
}
class Cast2 extends Throwable { 
	Lime lime;
}
class Lime {
	public Lime(){}
	public static makeLimenade(){
		System.out.println("Hi!");
	}
}
class runTest { 
	public static void throwEx() throws Cast1 {
		throw new Cast1();
	}
	public static void handleEx(Cast2 e) {
		e.lime.makeLimenade();
	}
	public static void main(String[] args) {
		try { 
			throwEx();
		} finally {
			handleEx();



