from datetime import date

from openg2p_fastapi_common.service import BaseService
from openg2p_registry_core.interfaces import G2PIdGeneratorInterface, IdAffix
from openg2p_registry_core.models.g2p_register import G2PRegister


class G2PIdGeneratorService(BaseService, G2PIdGeneratorInterface):
    """Functional-id affixes, matching the ATI sequences the Odoo registry uses.

    `data/ir_sequence_data.xml` defines the formats operators already recognise:

        g2p.crop.registry     CROP/REG/%(year)s/   padding 5   CROP/REG/2026/00012
        g2p.crop.production   CROP/PROD/%(year)s/  padding 5
        g2p.cluster           CLTR/%(year)s/       padding 5
        g2p.crop.infestation  PI/%(year)s/         padding 5

    The year is resolved when the id is minted, so a record created in 2027
    carries CROP/REG/2027/. The padding is the id-generator pool's idLength
    (5), set in the Helm values.
    """

    # register mnemonic -> sequence prefix, minus the year segment
    PREFIXES = {
        "cropsown": "CROP/REG",
        "production": "CROP/PROD",
        "cluster": "CLTR",
        "infestation": "PI",
    }

    def generate_prefix_suffix(
        self, g2p_register: G2PRegister, register_mnemonic: str
    ) -> IdAffix:
        mnemonic = (register_mnemonic or "").lower()
        prefix = self.PREFIXES.get(mnemonic)
        if prefix:
            return IdAffix(prefix=f"{prefix}/{date.today().year}/", suffix="")

        return IdAffix(prefix=f"CROP/{mnemonic.upper() or 'REC'}/{date.today().year}/", suffix="")
