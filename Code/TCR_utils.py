import subprocess
from biopandas.pdb import PandasPdb

def run_prodigy(pdb:str, selection:str = 'D,E C,A'):
    """
    USAGE:
        run_prodigy('8i5c.pdb', 'D,E C,A') D = TRA, E = TRB, C = peptide, A = MHC
    """
    subprocess.run(['Code/prodigy.sh', pdb, selection], text = True)

def get_prompt(pdbid:str):
    """
    Given a PDBID, gets the compound information, to be passed to a parser.

    Args:
        pdbid (str)_

    Returns:
        _str: information about the peptide (what kind of organism it belongs to)
    """
    pdpub = PandasPdb()
    pdb = pdpub.fetch_pdb(pdbid).df
    others = pdb['OTHERS']
    compound_info = others[others['record_name'] == 'COMPND']['entry'].values
    prompt = "".join(compound_info)
    return prompt

