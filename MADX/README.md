The MAD-X scripts present in this folder do not run. There are a set of issues.

- FHBBKE: sbend, l = 0; (Error message: +=+=+= fatal: bend with zero length: fhbbke)
-> Possible solution: FHBBKE and the other beam-beam elements are ignored

- Some matrix elements (e.g., ECSLP431) have an aperture definition: this is not allowed (Error message: +=+=+= fatal: illegal keyword: apertype)
-> Possible solution: ignore aperture definition, this can be added at a later stage, e.g., attaching it to a marker just after the matrix element

- The aperture definition of the collimator has a wrong sintax
-> Solution: Correct the sintax ({} brackets instead of () brackets for the aperture values)

- There is a drift (drift_eslp4000) that has a length l<0, this is not supperted by MAD-X (Error message: +=+=+= fatal: trying to add node with negative length to current sequence: drift_eslp4000:1).
-> Possible solution: set drift_eslp4000 with l=0 and apply an alignment error EALIGN from drift_eslp4000 to the end of DS<0

Including these modifications, the MAD-X script run correctly. It is therefor possible to save the sequence including at the end of the madx script:

```SAVE, SEQUENCE=LER, FILE='sler_1801_80_1.seq';```
