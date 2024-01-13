import rattish_manuals_helpers as RMH
import rattish_manuals_formating as RMF


commands = RMH.loadJson("commands")
namespaces = RMH.loadJson("namespaces")
readmeFill = RMH.loadJson("readme-filler")

for hexId in commands:
    if commands[hexId]["namespace"] in namespaces:
        RMH.createMdUsingTemplate(
            "command-details-template",
            {
                "namespace":commands[hexId]["namespace"].upper(),
                "asciihex":hexId,
                "asciidec":str(ord(commands[hexId]["char"])),
                "asciichar":commands[hexId]["char"].replace('`', '``'),
                "description":commands[hexId]["description"],
                "year":RMH.currentYear()
            },
            f'command-list/{hexId}.md'
        )

RMH.createMdUsingTemplate(
    "main-readme-template",
    {
        "intro":readmeFill["intro"],
        "details":readmeFill["details"],
        "langassumptions":RMF.basicListing(readmeFill["langassumptions"]),
        "commandslistwithnamespaces":RMF.namespacesCommandSection(
            namespaces,
            commands
        )+"\n"+RMF.unusedCommandsSection(
            namespaces,
            commands
        ),
        "examplesofrattish":RMF.exampleListing(RMH.listExamples()),
        "interpreterslist":RMF.itemListing(readmeFill["interpreters"]),
        "projectsconnected":RMF.projectsListing(readmeFill["projects"]),
        "year":RMH.currentYear()
    },
    'README.md'
)
