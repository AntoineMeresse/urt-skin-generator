models/weapons2/knife/knife_blade2 
{
	{
		map models/weapons2/knife/knife_blade2.jpg
	}
	{
		map models/weapons2/knife/platform_tint2.jpg
		blendfunc add
		tcGen environment 
		tcMod turb 0 0.25 0.5 0.2
		tcMod scroll 1
	}
	{
		map $lightmap
		blendFunc filter
	}
}
