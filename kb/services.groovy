class HelloFromGitGroovy extends Action {
    void onConfigure() {
        this.withLabel("Hello from git - Groovy").withDescription("Action defined in the git knowledge base.")
        this.withNoArgs()
        this.withResult(new StringType().withLabel("Hello"))
    }

    String onCall() {
        return "Hello from the Groovy git knowledge base"
    }
}

void onStartup() {
    // Required by Groovy.
}