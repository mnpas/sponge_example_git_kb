
def onAfterLoad():
    sponge.disable(HelloFromGit2)


class HelloFromGit(Action):
    def onConfigure(self):
        self.withLabel("Hello from git").withDescription(
            "Action defined in the git knowledge base.")
        self.withNoArgs().withResult(StringType().withLabel("Hello"))
        self.withFeature("icon", "git")

    def onCall(self):
        return "Hello from the git knowledge base 2 " + sponge.version
