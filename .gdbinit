source /home/cobra/Install/pwndbg/gdbinit.py
source /home/cobra/Install/Pwngdb/pwngdb.py
source /home/cobra/Install/Pwngdb/angelheap/gdbinit.py
source /home/cobra/Install/add_glibc_source/add_glibc_source.py

define hook-run
python
import angelheap
angelheap.init_angelheap()
end
end
