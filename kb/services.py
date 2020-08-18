
def onBeforeLoad():
    sponge.disable(HelloFromGit)


def onAfterLoad():
    pass


class HelloFromGit2(Action):
    def onConfigure(self):
        self.withLabel("Hello from git 2").withDescription(
            "Action defined in the git knowledge base.")
        self.withNoArgs().withResult(StringType().withLabel("Hello"))
        self.withFeature("icon", "git")

    def onCall(self):
        return "Hello from the git knowledge base " + sponge.version
