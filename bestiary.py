#!/usr/bin/python

import sys
import zlib
import xml.etree.ElementTree as ET

em_flags = [
 [ 'Goblins', 0, [ 4160, 4161, 4162, 4163, 4164, 4175, 4176, 4177, 4178, 4179, 4180, 4181 ] ],
 [ 'Hobgoblins', 1, [ 4165, 4166, 4167, 4168, 4169, 4175, 4176, 4177, 4178, 4179, 4180, 4181 ] ],
 [ 'Grimgoblins', 2, [ 4170, 4171, 4172, 4173, 4174, 4175, 4176, 4177, 4178, 4179, 4180, 4181, 4183 ] ],
 [ 'Greater Goblins', 50, [ 4832, 4833, 4834, 4835, 4836, 4175, 4176, 4177, 4181, 4842 ] ],
 [ 'Goblin Shamans', 50, [ 4832, 4833, 4834, 4835, 4836, 4175, 4176, 4177, 4843 ] ],
 [ 'Wolves', 3, [ 4192, 4193, 4194, 4195, 4196, 4207, 4208, 4209, 4210, 4211, 4212 ] ],
 [ 'Direwolves', 4, [ 4197, 4198, 4199, 4200, 4201, 4207, 4208, 4209, 4210, 4211, 4212 ] ],
 [ 'Hellhounds', 5, [ 4202, 4203, 4204, 4205, 4206, 4207, 4208, 4210, 4211, 4212 ] ],
 [ 'Wargs', 52, [ 4213, 4214, 4215, 4216, 4217, 4207, 4208, 4209, 4210, 4211, 4212 ] ],
 [ 'Garm', 52, [ 4218, 4219, 4220, 4221, 4222, 4207, 4208, 4209, 4210, 4223 ] ],
 [ 'Skeletons', 6, [ 4224, 4225, 4226, 4227, 4228, 4239, 4240 ] ],
 [ 'Skeleton Knights', 7, [ 4229, 4230, 4231, 4232, 4233, 4239, 4240 ] ],
 [ 'Skeleton Lords', 8, [ 4234, 4235, 4236, 4237, 4238, 4239, 4240 ] ],
 [ 'Skeleton Brutes', 53, [ 4864, 4865, 4866, 4867, 4868, 4239, 4240 ] ],
 [ 'Skeleton Mages', 9, [ 4384, 4385, 4386, 4387, 4388, 4239, 4240 ] ],
 [ 'Skeleton Sorcerers', 10, [ 4389, 4390, 4391, 4392, 4393, 4239, 4240 ] ],
 [ 'Golden Knights', 54, [ 4869, 4870, 4871, 4872, 4873, 4239, 4240, 4884 ] ],
 [ 'Silver Knights', 55, [ 4874, 4875, 4876, 4877, 4878, 4239, 4240 ] ],
 [ 'Living Armor', 56, [ 4879, 4880, 4881, 4882, 4883, 4239, 4240, 4885, 4886, 4887 ] ],
 [ 'Saurians', 11, [ 4256, 4257, 4258, 4259, 4260, 4276, 4277, 4279, 4903 ] ],
 [ 'Sulfur Saurians', 12, [ 4261, 4262, 4263, 4264, 4265, 4276, 4277, 4279, 4903 ] ],
 [ 'Geo Saurians', 13, [ 4266, 4267, 4268, 4269, 4270, 4276, 4277, 4903 ] ],
 [ 'Saurian Sages', 14, [ 4271, 4272, 4273, 4274, 4275, 4276, 4277, 4280, 4903 ] ],
 [ 'Pyre Saurians', 57, [ 4896, 4897, 4898, 4899, 4900, 4276, 4901, 4902, 4903 ] ],
 [ 'Undead', 15, [ 4288, 4289, 4290, 4291, 4292, 4308, 4309, 4310, 4311 ] ],
 [ 'Stout Undead', 16, [ 4293, 4294, 4295, 4296, 4297, 4308, 4309, 4310, 4311 ] ],
 [ 'Undead Warriors', 17, [ 4298, 4299, 4300, 4301, 4302, 4308, 4309, 4310, 4311 ] ],
 [ 'Giant Undead', 18, [ 4303, 4304, 4305, 4306, 4307, 4308, 4309, 4310, 4311 ] ],
 [ 'Poisoned Undead', 58, [ 4928, 4929, 4930, 4931, 4932, 4308, 4309, 4310 ] ],
 [ 'Banshees', 59, [ 4933, 4934, 4935, 4936, 4937, 4308, 4309, 4310, 4311, 4943, 4944, 4946 ] ],
 [ 'Eliminators', 60, [ 4938, 4939, 4940, 4941, 4942, 4310, 4945, 4947 ] ],
 [ 'Harpies', 19, [ 4320, 4321, 4322, 4323, 4324, 4340 ] ],
 [ 'Snow Harpies', 20, [ 4325, 4326, 4327, 4328, 4329, 4340, 4342 ] ],
 [ 'Succubi', 21, [ 4330, 4331, 4332, 4333, 4334, 4343 ] ],
 [ 'Gargoyles', 22, [ 4335, 4336, 4337, 4338, 4339, 4344 ] ],
 [ 'Strigoi', 61, [ 4960, 4961, 4962, 4963, 4964, 4970, 4972 ] ],
 [ 'Sirens', 62, [ 4965, 4966, 4967, 4968, 4969, 4971 ] ],
 [ 'Phantoms', 23, [ 4352, 4353, 4354, 4355, 4356, 4367 ] ],
 [ 'Phantasms', 24, [ 4357, 4358, 4359, 4360, 4361, 4367 ] ],
 [ 'Specters', 25, [ 4362, 4363, 4364, 4365, 4366, 4367 ] ],
 [ 'Wraiths', 63, [ 4370, 4371, 4372, 4373, 4374, 4367 ] ],
 [ 'Ogres', 30, [ 4416, 4417, 4418, 4419, 4420, 4421, 4422, 4423, 4424 ] ],
 [ 'Elder Ogres', 65, [ 4425, 4426, 4427, 4428, 4429, 4421, 4422, 4423, 4424 ] ],
 [ 'Cyclopes', 29, [ 4448, 4449, 4450, 4451, 4452, 4453, 4454, 4455, 4456, 4457 ] ],
 [ 'Gorecyclopes', 64, [ 4458, 4459, 4460, 4461, 4462, 4453, 4454, 4455, 4463 ] ],
 [ 'Golems', 31, [ 4480, 4481, 4482, 4483, 4484, 4490, 4491, 4492 ] ],
 [ 'Metal Golems', 32, [ 4485, 4486, 4487, 4488, 4489, 4490, 4491, 4492 ] ],
 [ 'Chimeras', 33, [ 4512, 4513, 4514, 4515, 4516, 4522, 4523, 4524, 4525 ] ],
 [ 'Gorechimeras', 34, [ 4517, 4518, 4519, 4520, 4521, 4522, 4523, 4524, 4525, 4526 ] ],
 [ 'Hydras', 35, [ 4544, 4545, 4546, 4547, 4548, 4554, 4555, 4556, 4557 ] ],
 [ 'Archydras', 36, [ 4549, 4550, 4551, 4552, 4553, 4554, 4555, 4556, 4557 ] ],
 [ 'Griffins', 37, [ 4576, 4577, 4578, 4579, 4580, 4586, 4587, 4588, 4589, 4590, 4591 ] ],
 [ 'Cockatrices', 38, [ 4581, 4582, 4583, 4584, 4585, 4587, 4589, 4592, 4593, 4594 ] ],
 [ 'Evil Eyes', 39, [ 4608, 4609, 4610, 4611, 4612, 4618, 4619, 4620, 4621 ] ],
 [ 'Vile Eyes', 40, [ 4613, 4614, 4615, 4616, 4617, 4618, 4621 ] ],
 [ 'Gazers', 66, [ 4624, 4625, 4626, 4627, 4628, 4618, 4621, 4634, 4635, 4636, 4637 ] ],
 [ 'Maneaters', 67, [ 4629, 4630, 4631, 4632, 4633, 4638, 4639 ] ],
 [ 'The Seneschal', 48, [ 4640, 4641, 4642, 4643, 4644 ] ],
 [ 'Wights', 41, [ 4672, 4673, 4674, 4675, 4676, 4682, 4683 ] ],
 [ 'Liches', 42, [ 4677, 4678, 4679, 4680, 4681, 4682, 4683 ] ],
 [ 'Dark Bishops', 68, [ 4684, 4685, 4686, 4687, 4688, 4683, 4694 ] ],
 [ 'Death', 69, [ 4689, 4690, 4691, 4692, 4693, 4695, 4696 ] ],
 [ 'The Dragon', 43, [ 4704, 4705, 4706, 4707, 4708, 4714, 4715, 4716, 4717, 4718 ] ],
 [ 'The Ur-Dragon', 44, [ 4709, 4710, 4711, 4712, 4713, 4714, 4716, 4717, 4718, 4719 ] ],
 [ 'Drakes', 45, [ 4736, 4737, 4738, 4739, 4740, 4714, 4716, 4717, 4718, 4720 ] ],
 [ 'Wyrms', 46, [ 4741, 4742, 4743, 4744, 4745, 4714, 4716, 4717, 4718, 4721 ] ],
 [ 'Wyverns', 47, [ 4746, 4747, 4748, 4749, 4750, 4714, 4716, 4717, 4718 ] ],
 [ 'Cursed Dragons', 70, [ 4751, 4752, 4753, 4754, 4755, 4714, 4716, 4717, 4718, 4756, 4757, 4758, 4759 ] ],
 [ 'Daimon', 71, [ 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000 ] ],
 [ 'Hostile Soldiers', 26, [ 4768, 4769, 4770, 4771, 4772 ] ],
 [ 'Hostile Bandits', 27, [ 4773, 4774, 4775, 4776, 4777 ] ],
 [ 'Enemy Wizard', 28, [ 4778, 4779, 4780, 4781, 4782 ] ],
 [ 'Enemy Person', 49, [ 4800, 4801, 4802, 4803, 4804 ] ]
]

counts = {
 4160: [ 60, 0, '' ],
 4161: [ 150, 0, '' ],
 4162: [ 300, 30, '' ],
 4163: [ 300, 150, '' ],
 4164: [ 300, 500, '' ],
 4165: [ 60, 0, '' ],
 4166: [ 150, 0, '' ],
 4167: [ 300, 20, '' ],
 4168: [ 300, 100, ' / Hobgoblin Tactics' ],
 4169: [ 300, 300, '' ],
 4170: [ 60, 0, '' ],
 4171: [ 150, 0, '' ],
 4172: [ 300, 20, '' ],
 4173: [ 300, 100, '' ],
 4174: [ 300, 300, '' ],
 4192: [ 60, 0, '' ],
 4193: [ 150, 0, '' ],
 4194: [ 300, 30, '' ],
 4195: [ 300, 150, '' ],
 4196: [ 300, 500, '' ],
 4197: [ 60, 0, '' ],
 4198: [ 210, 0, '' ],
 4199: [ 420, 30, '' ],
 4200: [ 420, 150, '' ],
 4201: [ 420, 500, '' ],
 4202: [ 60, 0, '' ],
 4203: [ 210, 0, '' ],
 4204: [ 420, 10, '' ],
 4205: [ 420, 50, '' ],
 4206: [ 420, 150, '' ],
 4213: [ 60, 0, '' ],
 4214: [ 210, 0, '' ],
 4215: [ 420, 20, '' ],
 4216: [ 420, 100, '' ],
 4217: [ 420, 300, '' ],
 4218: [ 60, 0, '' ],
 4219: [ 210, 0, '' ],
 4220: [ 420, 20, '' ],
 4221: [ 420, 100, '' ],
 4222: [ 420, 300, '' ],
 4224: [ 60, 0, '' ],
 4225: [ 150, 0, '' ],
 4226: [ 300, 20, '' ],
 4227: [ 300, 100, '' ],
 4228: [ 300, 300, '' ],
 4229: [ 60, 0, '' ],
 4230: [ 210, 0, '' ],
 4231: [ 420, 20, ' / Skeleton Knight Tactics' ],
 4232: [ 420, 100, '' ],
 4233: [ 420, 300, '' ],
 4234: [ 60, 0, '' ],
 4235: [ 240, 0, '' ],
 4236: [ 600, 4, '' ],
 4237: [ 600, 20, '' ],
 4238: [ 600, 50, '' ],
 4256: [ 60, 0, '' ],
 4257: [ 150, 0, '' ],
 4258: [ 300, 20, '' ],
 4259: [ 300, 100, '' ],
 4260: [ 300, 300, '' ],
 4261: [ 60, 0, '' ],
 4262: [ 150, 0, '' ],
 4263: [ 300, 15, ' / Saurian Tactics Vol. 1' ],
 4264: [ 300, 50, '' ],
 4265: [ 300, 150, '' ],
 4266: [ 60, 0, '' ],
 4267: [ 210, 0, '' ],
 4268: [ 420, 15, ' / Saurian Tactics Vol. 2' ],
 4269: [ 420, 50, '' ],
 4270: [ 420, 150, '' ],
 4271: [ 60, 0, '' ],
 4272: [ 210, 0, '' ],
 4273: [ 420, 8, '' ],
 4274: [ 420, 30, '' ],
 4275: [ 420, 100, '' ],
 4288: [ 60, 0, '' ],
 4289: [ 150, 0, '' ],
 4290: [ 300, 30, '' ],
 4291: [ 300, 150, '' ],
 4292: [ 300, 500, '' ],
 4293: [ 60, 0, '' ],
 4294: [ 150, 0, '' ],
 4295: [ 300, 15, ' / Undead Tactics Vol. 1' ],
 4296: [ 300, 50, '' ],
 4297: [ 300, 150, '' ],
 4298: [ 60, 0, '' ],
 4299: [ 150, 0, '' ],
 4300: [ 300, 30, '' ],
 4301: [ 300, 150, '' ],
 4302: [ 300, 500, '' ],
 4303: [ 60, 0, '' ],
 4304: [ 210, 0, '' ],
 4305: [ 420, 8, ' / Undead Tactics Vol. 2' ],
 4305: [ 420, 8, '' ],
 4306: [ 420, 30, '' ],
 4307: [ 420, 100, '' ],
 4320: [ 60, 0, '' ],
 4321: [ 150, 0, '' ],
 4322: [ 300, 20, '' ],
 4323: [ 300, 100, '' ],
 4324: [ 300, 300, '' ],
 4325: [ 60, 0, '' ],
 4326: [ 150, 0, '' ],
 4327: [ 300, 20, '' ],
 4328: [ 300, 100, '' ],
 4329: [ 300, 300, '' ],
 4330: [ 60, 0, '' ],
 4331: [ 150, 0, '' ],
 4332: [ 300, 10, '' ],
 4333: [ 300, 50, '' ],
 4334: [ 300, 150, '' ],
 4335: [ 60, 0, '' ],
 4336: [ 150, 0, '' ],
 4337: [ 300, 4, '' ],
 4338: [ 300, 20, '' ],
 4339: [ 300, 50, '' ],
 4352: [ 60, 0, '' ],
 4353: [ 150, 0, '' ],
 4354: [ 300, 4, ' / Ghost Tactics Vol. 2' ],
 4355: [ 300, 20, '' ],
 4356: [ 300, 50, '' ],
 4357: [ 60, 0, '' ],
 4358: [ 150, 0, '' ],
 4359: [ 300, 4, '' ],
 4360: [ 300, 20, '' ],
 4361: [ 300, 50, '' ],
 4362: [ 60, 0, '' ],
 4363: [ 150, 0, '' ],
 4364: [ 300, 4, ' / Ghost Tactics Vol. 1' ],
 4365: [ 300, 20, '' ],
 4366: [ 300, 50, '' ],
 4370: [ 60, 0, '' ],
 4371: [ 150, 0, '' ],
 4372: [ 300, 4, '' ],
 4373: [ 300, 15, '' ],
 4374: [ 300, 30, '' ],
 4384: [ 60, 0, '' ],
 4385: [ 150, 0, '' ],
 4386: [ 300, 8, '' ],
 4387: [ 300, 30, '' ],
 4388: [ 300, 100, '' ],
 4389: [ 60, 0, '' ],
 4390: [ 210, 0, '' ],
 4391: [ 420, 5, '' ],
 4392: [ 420, 30, '' ],
 4393: [ 420, 100, '' ],
 4416: [ 60, 0, '' ],
 4417: [ 240, 0, '' ],
 4418: [ 600, 4, '' ],
 4419: [ 600, 20, '' ],
 4420: [ 600, 50, '' ],
 4425: [ 60, 0, '' ],
 4426: [ 240, 0, '' ],
 4427: [ 600, 4, '' ],
 4428: [ 600, 20, '' ],
 4429: [ 600, 50, '' ],
 4448: [ 60, 0, '' ],
 4449: [ 240, 0, '' ],
 4450: [ 600, 3, ' / Cyclops Tactics' ],
 4451: [ 600, 10, '' ],
 4452: [ 600, 30, '' ],
 4458: [ 60, 0, '' ],
 4459: [ 240, 0, '' ],
 4460: [ 600, 4, '' ],
 4461: [ 600, 20, '' ],
 4462: [ 600, 50, '' ],
 4480: [ 60, 0, '' ],
 4481: [ 240, 0, '' ],
 4482: [ 600, 2, ' / Golem Tactics' ],
 4483: [ 600, 5, '' ],
 4484: [ 600, 15, '' ],
 4485: [ 60, 0, '' ],
 4486: [ 240, 0, '' ],
 4487: [ 600, 1, '' ],
 4488: [ 600, 3, '' ],
 4489: [ 600, 7, '' ],
 4512: [ 60, 0, '' ],
 4513: [ 240, 0, '' ],
 4514: [ 600, 3, ' / Chimera Tactics' ],
 4515: [ 600, 10, '' ],
 4516: [ 600, 30, '' ],
 4517: [ 60, 0, '' ],
 4518: [ 240, 0, '' ],
 4519: [ 600, 3, '' ],
 4520: [ 600, 10, '' ],
 4521: [ 600, 30, '' ],
 4544: [ 60, 0, '' ],
 4545: [ 240, 0, '' ],
 4546: [ 600, 1, ' / Hydra Tactics' ],
 4547: [ 600, 3, '' ],
 4548: [ 600, 7, '' ],
 4549: [ 60, 0, '' ],
 4550: [ 240, 0, '' ],
 4551: [ 600, 1, '' ],
 4552: [ 600, 3, '' ],
 4553: [ 600, 7, '' ],
 4576: [ 60, 0, '' ],
 4577: [ 240, 0, '' ],
 4578: [ 600, 2, '' ],
 4579: [ 600, 5, '' ],
 4580: [ 600, 15, '' ],
 4581: [ 60, 0, '' ],
 4582: [ 240, 0, '' ],
 4583: [ 600, 2, '' ],
 4584: [ 600, 5, '' ],
 4585: [ 600, 15, '' ],
 4608: [ 60, 0, '' ],
 4609: [ 240, 0, '' ],
 4610: [ 600, 2, '' ],
 4611: [ 600, 5, '' ],
 4612: [ 600, 15, '' ],
 4613: [ 60, 0, '' ],
 4614: [ 240, 0, '' ],
 4615: [ 600, 3, '' ],
 4616: [ 600, 10, '' ],
 4617: [ 600, 30, '' ],
 4624: [ 60, 0, '' ],
 4625: [ 240, 0, '' ],
 4626: [ 600, 2, '' ],
 4627: [ 600, 5, '' ],
 4628: [ 600, 15, '' ],
 4629: [ 60, 0, '' ],
 4630: [ 240, 0, '' ],
 4631: [ 600, 3, '' ],
 4632: [ 600, 10, '' ],
 4633: [ 600, 30, '' ],
 4640: [ 60, 0, '' ],
 4641: [ 240, 0, '' ],
 4642: [ 600, 1, '' ],
 4643: [ 600, 2, '' ],
 4644: [ 600, 3, '' ],
 4672: [ 60, 0, '' ],
 4673: [ 240, 0, '' ],
 4674: [ 600, 3, ' / Wight Tactics' ],
 4675: [ 600, 10, '' ],
 4676: [ 600, 30, '' ],
 4677: [ 60, 0, '' ],
 4678: [ 240, 0, '' ],
 4679: [ 600, 2, ' / Lich Tactics' ],
 4680: [ 600, 5, '' ],
 4681: [ 600, 15, '' ],
 4684: [ 60, 0, '' ],
 4685: [ 240, 0, '' ],
 4686: [ 600, 3, '' ],
 4687: [ 600, 10, '' ],
 4688: [ 600, 30, '' ],
 4689: [ 60, 0, '' ],
 4690: [ 240, 0, '' ],
 4691: [ 600, 1, '' ],
 4692: [ 600, 3, '' ],
 4693: [ 600, 6, '' ],
 4704: [ 60, 0, '' ],
 4705: [ 180, 0, '' ],
 4706: [ 600, 1, '' ],
 4707: [ 600, 2, '' ],
 4708: [ 600, 3, '' ],
 4709: [ 60, 0, '' ],
 4710: [ 240, 0, '' ],
 4711: [ 600, 1, '' ],
 4712: [ 600, 2, '' ],
 4713: [ 600, 3, '' ],
 4736: [ 60, 0, '' ],
 4737: [ 240, 0, '' ],
 4738: [ 600, 2, '' ],
 4739: [ 600, 5, '' ],
 4740: [ 600, 15, '' ],
 4741: [ 60, 0, '' ],
 4742: [ 240, 0, '' ],
 4743: [ 600, 2, '' ],
 4744: [ 600, 5, '' ],
 4745: [ 600, 15, '' ],
 4746: [ 60, 0, '' ],
 4747: [ 240, 0, '' ],
 4748: [ 600, 2, '' ],
 4749: [ 600, 5, '' ],
 4750: [ 600, 15, '' ],
 4751: [ 60, 0, '' ],
 4752: [ 240, 0, '' ],
 4753: [ 600, 2, '' ],
 4754: [ 600, 5, '' ],
 4755: [ 600, 15, '' ],
 4768: [ 60, 0, '' ],
 4769: [ 150, 0, '' ],
 4770: [ 300, 10, '' ],
 4771: [ 300, 50, '' ],
 4772: [ 300, 150, '' ],
 4773: [ 60, 0, '' ],
 4774: [ 150, 0, '' ],
 4775: [ 300, 30, '' ],
 4776: [ 300, 150, '' ],
 4777: [ 300, 500, '' ],
 4778: [ 60, 0, '' ],
 4779: [ 150, 0, '' ],
 4780: [ 300, 10, '' ],
 4781: [ 300, 50, '' ],
 4782: [ 300, 150, '' ],
 4800: [ 60, 0, '' ],
 4801: [ 150, 0, '' ],
 4802: [ 300, 10, '' ],
 4803: [ 300, 50, '' ],
 4804: [ 300, 150, '' ],
 4832: [ 60, 0, '' ],
 4832: [ 60, 0, '' ],
 4833: [ 150, 0, '' ],
 4833: [ 150, 0, '' ],
 4834: [ 300, 30, '' ],
 4834: [ 300, 30, '' ],
 4835: [ 300, 150, '' ],
 4835: [ 300, 150, '' ],
 4836: [ 300, 400, '' ],
 4836: [ 300, 400, '' ],
 4864: [ 60, 0, '' ],
 4865: [ 210, 0, '' ],
 4866: [ 420, 20, '' ],
 4867: [ 420, 100, '' ],
 4868: [ 420, 300, '' ],
 4869: [ 60, 0, '' ],
 4870: [ 240, 0, '' ],
 4871: [ 600, 15, '' ],
 4872: [ 1200, 50, '' ],
 4873: [ 1200, 100, '' ],
 4874: [ 60, 0, '' ],
 4875: [ 240, 0, '' ],
 4876: [ 600, 15, '' ],
 4877: [ 1200, 50, '' ],
 4878: [ 1200, 100, '' ],
 4879: [ 60, 0, '' ],
 4880: [ 240, 0, '' ],
 4881: [ 600, 10, '' ],
 4882: [ 1200, 25, '' ],
 4883: [ 1200, 50, '' ],
 4896: [ 60, 0, '' ],
 4897: [ 210, 0, '' ],
 4898: [ 420, 20, '' ],
 4899: [ 420, 100, '' ],
 4900: [ 420, 300, '' ],
 4928: [ 60, 0, '' ],
 4929: [ 210, 0, '' ],
 4930: [ 420, 20, '' ],
 4931: [ 420, 100, '' ],
 4932: [ 420, 300, '' ],
 4933: [ 60, 0, '' ],
 4934: [ 210, 0, '' ],
 4935: [ 420, 20, '' ],
 4936: [ 420, 100, '' ],
 4937: [ 420, 300, '' ],
 4938: [ 60, 0, '' ],
 4939: [ 210, 0, '' ],
 4940: [ 420, 15, '' ],
 4941: [ 420, 30, '' ],
 4942: [ 420, 60, '' ],
 4960: [ 60, 0, '' ],
 4961: [ 150, 0, '' ],
 4962: [ 300, 15, '' ],
 4963: [ 300, 50, '' ],
 4964: [ 300, 100, '' ],
 4965: [ 60, 0, '' ],
 4966: [ 150, 0, '' ],
 4967: [ 300, 15, '' ],
 4968: [ 300, 50, '' ],
 4969: [ 300, 100, '' ],
 4992: [ 60, 0, '' ],
 4993: [ 240, 0, '' ],
 4994: [ 600, 1, '' ],
 4995: [ 600, 3, '' ],
 4996: [ 600, 10, '' ]
}

unique = {
 4175: [ 0, 5, 'Observe when Burning' ],
 4176: [ 1, 20, 'Stagger' ],
 4177: [ 2, 3, 'Inflict Blind' ],
 4178: [ 3, 5, 'Inflict Frozen' ],
 4179: [ 4, 10, 'Kill one with a shield' ],
 4180: [ 5, 10, 'Kill one with a horn' ],
 4181: [ 6, 10, 'Kill the leader / Goblin Strategies' ],
 4182: [ 7, 5, '' ],
 4183: [ 8, 5, 'Observe thrust attack' ],
 4207: [ 9, 2, 'Block lunge attack / Wolf Strategy Vol. 1' ],
 4208: [ 10, 5, 'Observe calling for help' ],
 4209: [ 11, 3, 'Inflict Drenched / Wolf Strategy Vol. 2' ],
 4210: [ 12, 3, 'Inflict Torpor / Wolf Strategy Vol. 3' ],
 4211: [ 13, 3, 'Inflict Silence' ],
 4212: [ 14, 5, 'Observe when Burning' ],
 4239: [ 15, 50, 'Damage with Holy / Skeleton Strategies' ],
 4240: [ 16, 50, 'Damage with Blunt' ],
 4276: [ 17, 5, 'Sever the tail / Saurian Strategy Vol. 1' ],
 4277: [ 18, 50, 'Damage with Ice' ],
 4279: [ 19, 5, 'Observe when Burning' ],
 4280: [ 20, 2, 'Inflict Silence / Saurian Strategy Vol. 2' ],
 4308: [ 21, 50, 'Damage with Fire' ],
 4309: [ 22, 50, 'Damage with Holy / Undead Strategy Vol. 1' ],
 4310: [ 23, 20, 'Hit head' ],
 4311: [ 24, 2, 'Grapple undead that grapple / Undead Strategy Vol. 2' ],
 4340: [ 25, 5, 'Burn to prevent flying / Harpy Strategies' ],
 4341: [ 26, 2, '' ],
 4342: [ 27, 50, 'Damage with Fire' ],
 4343: [ 28, 50, 'Damage with Holy' ],
 4344: [ 29, 50, 'Damage with Lightning' ],
 4367: [ 30, 10, 'Damage with Holy' ],
 4368: [ 31, 3, '' ],
 4453: [ 32, 2, 'Climb leg to get it to lift its leg' ],
 4454: [ 33, 5, 'Knockdown' ],
 4455: [ 34, 3, 'Disarm / Cyclops Strategy Vol. 1' ],
 4456: [ 35, 5, 'Observe Thundershock' ],
 4457: [ 36, 5, 'Break tusks / Cyclops Strategy Vol. 2' ],
 4421: [ 37, 3, 'Make it guard its face' ],
 4422: [ 38, 5, '? / Ogre Strategy Vol. 1' ],
 4423: [ 39, 3, 'Knockdown by climing when it does an attack' ],
 4424: [ 40, 2, '? / Ogre Strategy Vol. 2' ],
 4490: [ 41, 50, 'Damage with Blunt' ],
 4491: [ 42, 3, '? / Golem Strategy Vol. 1' ],
 4492: [ 43, 2, 'Hit head when it uses beam / Golem Strategy Vol. 2' ],
 4522: [ 44, 2, 'Kill the snake head / Chimera Strategy Vol. 1' ],
 4523: [ 45, 50, 'Damage lion with Magick' ],
 4524: [ 46, 50, 'Damage goat with Physical' ],
 4525: [ 47, 3, 'Inflict Silence / Chimera Strategy Vol. 2' ],
 4526: [ 48, 5, 'Burn cut snake head' ],
 4554: [ 49, 3, 'Sever a head / Hydra Strategy Vol. 1' ],
 4555: [ 50, 50, 'Damage with Fire' ],
 4556: [ 51, 3, 'Burn a cut head stump / Hydra Strategy Vol. 2' ],
 4557: [ 52, 2, 'Barrel trick' ],
 4586: [ 53, 3, 'Observe big crash' ],
 4587: [ 54, 30, 'Hit the head' ],
 4588: [ 55, 3, 'Observe flailing when grappled / Griffin Strategy Vol. ' ],
 4589: [ 56, 2, 'Block beak attack / Griffin Strategy Vol. 3' ],
 4590: [ 57, 2, 'Have 3 or more climb' ],
 4591: [ 58, 2, 'Lure down with a carcass / Griffin Strategy Vol. 2' ],
 4592: [ 59, 50, 'Damage with Lightning' ],
 4593: [ 60, 2, 'Observe when Blind / Cockatrice Strategy Vol. 1' ],
 4594: [ 61, 3, 'Interrupt by attacking throat / Cockatrice Strategy Vol. 2' ],
 4618: [ 62, 50, 'Damage with Holy' ],
 4619: [ 63, 3, '? / Evil Eye Strategy Vol. 1' ],
 4620: [ 64, 3, "Hit when it's charging / Evil Eye Strategy Vol. 2" ],
 4621: [ 65, 3, 'Knockdown' ],
 4623: [ 66, 1, '' ],
 4682: [ 67, 50, 'Damage with Holy' ],
 4683: [ 68, 50, 'Damage with Blunt' ],
 4714: [ 69, 3, 'Knockdown by hitting heart' ],
 4715: [ 70, 50, 'Damage with Dark' ],
 4716: [ 71, 10, 'Stagger / Draconian Strategy Vol. 1' ],
 4717: [ 72, 3, "Knockdown while it's casting" ],
 4718: [ 73, 3, 'Hit head to stop breath attack / Draconian Strategy Vol. 2' ],
 4719: [ 74, 50, 'Damage with Holy' ],
 4720: [ 75, 50, 'Damage with Ice' ],
 4721: [ 76, 50, 'Damage with Fire' ],
 4842: [ 77, 50, 'Damage with Lightning' ],
 4843: [ 78, 30, 'Damage with Physical' ],
 4223: [ 79, 50, 'Damage with Lightning' ],
 4884: [ 80, 30, 'Obseve resurrection' ],
 4885: [ 81, 30, 'Attck from behind' ],
 4886: [ 82, 30, 'Damage Armor' ],
 4887: [ 83, 30, 'Damage Ghost' ],
 4901: [ 84, 5, 'Inflict Drenched' ],
 4902: [ 85, 10, 'Extinguish flame' ],
 4903: [ 86, 50, 'Attack while climbing' ],
 4943: [ 87, 50, 'Damage with Ice' ],
 4944: [ 88, 30, 'Damage with Physical' ],
 4946: [ 89, 30, 'Damage Eliminator with Magick' ],
 4945: [ 90, 10, 'Observe Banshee scream' ],
 4947: [ 91, 5, 'Observe stomp attack' ],
 4970: [ 92, 50, 'Damage with Ice' ],
 4972: [ 94, 10, 'Observe tail turning red' ],
 4971: [ 93, 50, 'Damage with Dark' ],
 4463: [ 95, 50, 'Damage with Ice' ],
 4634: [ 96, 50, 'Hit eye directly' ],
 4635: [ 97, 5, 'Observe poisoned cloud' ],
 4636: [ 98, 1, 'Stun with Spire Tentacle' ],
 4637: [ 99, 1, 'Destroy Great Cannon tentacles' ],
 4638: [ 100, 10, 'Get bonus loot' ],
 4639: [ 101, 1, 'Open Maneater chest' ],
 4694: [ 102, 50, 'Damage with Holy' ],
 4695: [ 103, 1, 'Observe scythe attack' ],
 4696: [ 104, 2, 'Observe it fleeing' ],
 4756: [ 105, 10, 'Observe the Dark Bishop revive it' ],
 4757: [ 106, 10, 'Observe the Dark Bishop possess it' ],
 4758: [ 107, 20, 'Observe items rotting' ],
 4759: [ 108, 50, 'Damage with Holy' ],
 4997: [ 109, 10, 'Hit first form head' ],
 4998: [ 110, 20, 'Damage with Holy' ],
 4999: [ 111, 30, 'Hit second form head' ],
 5000: [ 112, 1, 'Observe vortex' ]
}

for arg in sys.argv[1:]:
	f = open(arg, 'rb')
	f.seek(32)
	tree = ET.fromstring(zlib.decompress(f.read()))
	f.close()
	obj = tree.find('.//array[@name="mStudyFlag"]')
	cnt = tree.find('.//array[@name="mStudyData.KillCnt"]')
	uni = tree.find('.//array[@name="mStudyData.UniqueCnt"]')
	sec = tree.find('.//array[@name="mStudyData.EncountFrame"]')
	flags = { }
	n = 130 * 32

	for i in range(130,157):
		v = int(obj[i].get('value'))

		for j in range(32):
			flags[n] = v & 1
			v >>= 1
			n += 1

	for l in em_flags:
		print(l[0])
		s = int(float(sec[l[1]].get('value')) / 30.0);
		k = cnt[l[1]].get('value')
		for f in l[2]:
			if flags[f] == 0:
				if f in unique:
					u = unique[f]
					k = uni[u[0]].get('value');
					print(" %d: %s/%d %s" % (f, k, u[1], u[2]))
				else:
					c = counts[f]
					if c[1] > 0:
						print(" %d: %d/%d seconds and %s/%d kills%s" % (f, s, c[0], k, c[1], c[2]))
					else:
						print(" %d: %d/%d seconds%s" % (f, s, c[0], c[2]))
