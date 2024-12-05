# https://adventofcode.com/2017/day/3
from solutions.challenge import Challenge
import numpy as np


class Day03(Challenge):
    @staticmethod
    def solve_part1(src,dst=1):
        num_tiers = 0
        tier_max = 1
        while tier_max < src:
            tier_max += 8*num_tiers
            num_tiers += 1
        arr = np.ones((1,1),dtype=int)
        for tier in range(1,num_tiers):
            tier_min = arr[-1,-1]+1
            tier_max = arr[-1,-1]+tier*8
            tier_vals = np.arange(tier_min,tier_max+1)
            arr = np.vstack((
                tier_vals[arr.shape[0]:sum(arr.shape)+2][::-1].reshape(arr.shape[0]+2),
                np.hstack((
                    tier_vals[sum(arr.shape)+2:sum(arr.shape)+2+arr.shape[0]][::-1].reshape((arr.shape[0],1)),
                    arr,
                    tier_vals[:arr.shape[0]].reshape((arr.shape[0],1))
                )),
                tier_vals[sum(arr.shape)+arr.shape[0]+2:].reshape(arr.shape[1]+2)
            ))
        src_idx = np.argwhere(arr == src)[0]
        dst_idx = np.argwhere(arr == dst)[0]
        return np.sum(np.abs(src_idx-dst_idx))

    @staticmethod
    def solve_part2(goal):
        arr = np.ones((1,1),dtype=int)
        while True:
            # append left
            arr = np.hstack((arr,np.zeros((arr.shape[0],1),dtype=int)))
            for i in range(arr.shape[0])[::-1]:
                arr[i,-1] = np.sum(arr[max(i-1,0):min(i+2,arr.shape[0]),-2:])
                if arr[i,-1] > goal:
                    return arr[i,-1]
            # append top
            arr = np.vstack((np.zeros((1,arr.shape[1]),dtype=int),arr))
            for j in range(arr.shape[1])[::-1]:
                arr[0,j] = np.sum(arr[:2,max(j-1,0):min(j+2,arr.shape[0])])
                if arr[0,j] > goal:
                    return arr[0,j]
            # append right
            arr = np.hstack((np.zeros((arr.shape[0],1),dtype=int),arr))
            for i in range(arr.shape[0]):
                arr[i,0] = np.sum(arr[max(i-1,0):min(i+2,arr.shape[0]),:2])
                if arr[i,0] > goal:
                    return arr[i,0]
            # append bottom
            arr = np.vstack((arr,np.zeros((1,arr.shape[1]),dtype=int)))
            for j in range(arr.shape[1]):
                arr[-1,j] = np.sum(arr[-2:,max(j-1,0):min(j+2,arr.shape[0])])
                if arr[-1,j] > goal:
                    return arr[-1,j]


if __name__ == "__main__":
    Day03().solve_all(277678)
