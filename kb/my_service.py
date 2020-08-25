class OsGetDiskSpaceInfo(Action):
    def onConfigure(self):
        self.withLabel("Get disk space info").withDescription(
            "Returns the disk space info.")
        self.withNoArgs().withResult(StringType().withFormat(
            "console").withLabel("Disk space info"))
        self.withFeature("icon", "console")

    def onCall(self):
        return sponge.process("df", "-h").outputAsString().run().outputString
