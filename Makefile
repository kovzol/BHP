ZTEXT_DIR=modules/texts/ztext/bhpgnt
NT_BZZ=$(ZTEXT_DIR)/nt.bzz

all: $(NT_BZZ)

BHP_osis.xml: BHP_Data.txt txt2osis.py
	python3 txt2osis.py > $@
$(NT_BZZ): BHP_osis.xml
	mkdir -p $(ZTEXT_DIR)
	osis2mod $(ZTEXT_DIR) $< -z z -v LXX
	@echo "Copy $(ZTEXT_DIR) to your <SWORD_DIR> and bhpgnt.conf to <SWORD_DIR>/mods.d to finalize your installation."
