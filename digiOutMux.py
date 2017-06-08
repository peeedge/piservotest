import u6
import time
import sys

d = u6.U6()
d.getCalibrationData()

#on15 = (u6.BitDirWrite(15, 1), u6.BitStateWrite(15, 1))
##off15 = (u6.BitDirWrite(15, 1), u6.BitStateWrite(15, 0))
#on16 = (u6.BitDirWrite(16, 1), u6.BitStateWrite(16, 1))
#off16 = (u6.BitDirWrite(16, 1), u6.BitStateWrite(16, 0))
#on17 = (u6.BitDirWrite(17, 1), u6.BitStateWrite(17, 1))
#off17 = (u6.BitDirWrite(17, 1), u6.BitStateWrite(17, 0))
#cmdList=[]

# for q in xrange(int(sys.argv[1])):
# 	time.sleep(1)
# 	state15 = (q%8)//4
# 	if state15 >= 1:
# 		s15 = 1
# 	else:
# 		s15 = 0

# 	state16 = (q%4)//2
# 	if state16 >= 1:
# 		s16 = 1
# 	else:
# 		s16 = 0

# 	state17 = (q%2)

# 	mux15 = (u6.BitDirWrite(20, 1), u6.BitStateWrite(20, s20))
# 	mux16 = (u6.BitDirWrite(21, 1), u6.BitStateWrite(21, s21))
# 	mux17 = (u6.BitDirWrite(22, 1), u6.BitStateWrite(22, state22))

# 	cmdList.append(mux20)
# 	cmdList.append(mux21)
# 	cmdList.append(mux22)
# 	d.getFeedback(cmdList)
# 	cmdList = []
# 	print(s20, s21, state22)


#cmdList.append(on15)
###cmdList.append(on16)
#cmdList.append(off17)
#d.getFeedback(cmdList)

# cmdList.append(on20)
# cmdList.append(off21)
# cmdList.append(off22)
# d.getFeedback(cmdList)

# cmdList.append(off20)
# cmdList.append(off21)
# cmdList.append(on22)
# d.getFeedback(cmdList)

d.setDOState(16,1)
d.setDOState(17,0)