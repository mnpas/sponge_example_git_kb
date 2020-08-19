
def onAfterLoad():
    pass  # sponge.disable(HelloFromGit2)


class HelloWorldActionPython(Action):
    def onConfigure(self):
        self.withLabel(
            "Hello world git - Python").withDescription("Returns a greeting text.")
        self.withArg(StringType("name").withLabel(
            "Your name").withDescription("Type your name."))
        self.withResult(StringType().withLabel(
            "Greeting").withDescription("The greeting text."))
        self.withFeature("icon", "git")

    def onCall(self, name):
        return "Hello World! Hello {}!".format(name)

# class HelloFromGit(Action):
#     def onConfigure(self):
#         self.withLabel("Hello from git").withDescription(
#             "Action defined in the git knowledge base.")
#         self.withNoArgs().withResult(StringType().withLabel("Hello"))
#         self.withFeature("icon", "git")

#     def onCall(self):
#         return "Hello from the git knowledge base 2 " + sponge.version
