import numpy as np
import xobjects as xo
import xtrack as xt
import xpart as xp
from cpymad.madx import Madx
import json
from pathlib import Path
from generic_parser import EntryPointParameters, entrypoint

def get_params():
    params = EntryPointParameters()
    params.add_parameter(
        name="sequence_file",
        type=str,
        required=True,
        help="Path to the madx sequence file.",
    )

    return params

@entrypoint(get_params(), strict=True)
def main(opt):

    filename = Path(opt.sequence_file)
    with Madx() as mad:

        mad.input(
            f"""
                CALL, FILE="{filename}";

                pbeam :=   4;
                Npart := 35101697183.518524;
                ! EXbeam = 4.6e-9;
                ! EYbeam = 30e-12;

                Ebeam := sqrt( pbeam^2 + emass^2 );

                BEAM, PARTICLE=POSITRON, NPART=Npart, ENERGY=Ebeam, RADIATE=True;

                USE, SEQUENCE = LER;

            """
        )

        madsequence = mad.sequence['LER']
        line = xt.Line.from_madx_sequence(madsequence, install_apertures=True, allow_thick=True)
        line.particle_ref = xp.Particles(q0=1, mass0=xp.ELECTRON_MASS_EV, gamma0=madsequence.beam.gamma)

    # Save to json
    with open('sler_1801_80_1.json', 'w') as fid:
        json.dump(line.to_dict(), fid, cls=xo.JEncoder)

# Script Mode ------------------------------------------------------------------

if __name__ == "__main__":
    main()