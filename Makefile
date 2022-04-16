# Issue "make" to create a Sword module, and "make BHPGNT.zip" to create it as a .zip bundle.

ZTEXT_DIR=modules/texts/ztext/bhpgnt
NT_BZZ=$(ZTEXT_DIR)/nt.bzz
NT_BZV=$(ZTEXT_DIR)/nt.bzv
NT_BZS=$(ZTEXT_DIR)/nt.bzs
NT=$(NT_BZZ) $(NT_BZV) $(NT_BZS)

all: $(NT)

BHP_osis.xml: BHP_Data.txt txt2osis.py
	python3 txt2osis.py > $@
$(NT): BHP_osis.xml
	mkdir -p $(ZTEXT_DIR)
	osis2mod $(ZTEXT_DIR) $< -z z -v LXX
	@echo "Copy $(ZTEXT_DIR) and mods.d/bhpgnt.conf to your <SWORD_DIR> to finalize your installation."

BHPGNT.zip: $(NT) mods.d/bhpgnt.conf
	zip -9r $@ $^
