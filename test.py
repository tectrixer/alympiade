
times = [[267, 235, 236, 738], [201, 169, 190, 560], [232, 200, 221, 653], [213, 151, 182, 546], [197, 0, 191, 388], [159, 0, 168, 327], [0, 111, 144, 255], [167, 124, 136, 427], [0, 102, 149, 251], [284, 0, 253, 537], [266, 0, 0, 266], [0, 0, 0, 0], [282, 84, 251, 617], [265, 63, 234, 562], [220, 0, 189, 409], [0, 114, 223, 337], [0, 116, 0, 116], [224, 101, 214, 539], [234, 88, 203, 525], [0, 238, 0, 238], [218, 246, 0, 464], [202, 230, 0, 432], [195, 223, 0, 418], [179, 0, 0, 179], [0, 192, 0, 192], [178, 206, 76, 460], [148, 0, 87, 235], [129, 162, 61, 352], [0, 276, 217, 493], [0, 268, 209, 477], [0, 253, 194, 447], [0, 0, 183, 183], [0, 223, 164, 387], [0, 0, 0, 0], [75, 182, 110, 367], [93, 0, 95, 188], [110, 140, 84, 334], [126, 143, 109, 378], [141, 124, 132, 397], [158, 109, 153, 420], [173, 95, 172, 440], [183, 85, 182, 450], [196, 71, 176, 443], [0, 0, 0, 0], [170, 83, 139, 392], [146, 99, 115, 360], [176, 131, 152, 459], [167, 124, 136, 427], [128, 119, 140, 387], [83, 170, 151, 404], [176, 174, 205, 555], [0, 113, 160, 273], [172, 125, 0, 297], [135, 131, 0, 266], [121, 145, 156, 422], [126, 139, 161, 426], [0, 145, 176, 321], [114, 153, 147, 414], [99, 143, 135, 377]]
least_difference = 1000
for time in times:
     if time[0] != 0 & time[1] != 0 & time[2] != 0: 
        biggest_value = 0
        if Math.abs(time[0] - time[1]) > Math.abs(time[0] - time[2]):
            if Math.abs(time[1] - time[2]) > Math.abs(time[0] - time[2]):
                if Math.abs(time[0] - time[2]) < least_difference:
                    least_difference = Math.abs(time[0] - time[2])
            elif Math.abs(time[1] - time[2]) < least_difference:
                least_difference = Math.abs(time[1] - time[2])
        elif Math.abs(time[0] - time[1]) > Math.abs(time[1] - time[2]):
            if Math.abs(time[1] - time[2]) < least_difference:
                    least_difference = Math.abs(time[1] - time[2])
        elif Math.abs(time[0] - time[1]) < least_difference:
                    least_difference = Math.abs(time[0] - time[1])
print(least_difference)
