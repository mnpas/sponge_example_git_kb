class HelloWorldActionGroovy extends Action {
    void onConfigure() {
        this.withLabel("Hello world - Groovy").withDescription("Returns a greeting text.")
        this.withArg(new StringType("name").withLabel("Your name").withDescription("Type your name."))
        this.withResult(new StringType().withLabel("Greeting").withDescription("The greeting text."))
    }

    String onCall(String name) {
        return "Hello World! Hello $name!"
    }
}

// Required by Groovy.
void onLoad() {
}