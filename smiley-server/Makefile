all: copysrc build

build: compile
	docker build -t smiley src/

copysrc: compile
	zip static/adminserver.zip src/worker.c src/adminserver.c src/msgstructs.h src/adminserver src/worker
	../utils/cdnify static/adminserver.zip

run:
	docker run -d -p 8091:1337 -t smiley

compile:
	gcc src/adminserver.c src/msgstructs.h -m32 -funit-at-a-time -ftree-forwprop -ftree-ter -fipa-pure-const -fipa-profile -fmerge-constants -malign-double -ftree-bit-ccp -fdse -fauto-inc-dec -fif-conversion -ftree-sra -fbranch-count-reg -ftree-dse -ftree-sink -ftree-copyrename -ftree-phiprop -fshrink-wrap -ftree-copy-prop -ftree-fre -fsplit-wide-types -ftree-pta -ftree-dominator-opts -ftree-ccp -fcompare-elim -fif-conversion2 -ftree-slsr -fdefer-pop -fforward-propagate -fipa-reference -ftree-dce -o src/adminserver
	gcc src/worker.c src/msgstructs.h -m32 -ftree-ter -ftree-dominator-opts -fcprop-registers -fcombine-stack-adjustments -ftree-sra -ftree-forwprop -fipa-profile -ftree-ccp -fdse -ftree-fre -ftree-pta -ftree-sink -ftree-copy-prop -fauto-inc-dec -fguess-branch-probability -fmove-loop-invariants -fmerge-constants -fshrink-wrap -fsplit-wide-types -fforward-propagate -ftree-dce -ftree-bit-ccp -fdce -ftree-phiprop -fbranch-count-reg -fif-conversion2 -finline-functions-called-once -fif-conversion -fdefer-pop -fcompare-elim -o src/worker

