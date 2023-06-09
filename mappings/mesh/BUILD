wget ftp://nlmpubs.nlm.nih.gov/online/mesh/MESH_FILES/xmlmesh/desc*.gz
wget ftp://nlmpubs.nlm.nih.gov/online/mesh/MESH_FILES/xmlmesh/pa*.xml


wget ftp://nlmpubs.nlm.nih.gov/online/mesh/rdf/2021/mesh*.nt.gz

python3 ../../src/mesh_to_registry_id.py desc*.gz | awk '$2 != 0' > mesh_to_registry_id.txt

touch MESH_COMPLETE
