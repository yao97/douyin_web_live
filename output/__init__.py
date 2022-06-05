from output.print import Print
from output.debug import DebugWriter
from output.xml import XMLWriter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from output.IOutput import IOutput

OUTPUTER: "list[IOutput]" = [
    Print(),
    XMLWriter(),
    DebugWriter()
]
