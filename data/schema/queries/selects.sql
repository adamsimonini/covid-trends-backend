-- TABLE JOIN COMMANDS

-- join health regions and provinces
SELECT * FROM health_regions hr
LEFT JOIN provinces p
ON p.province_code = hr.fk_province_code;

-- join health regions, provinces, and regions
WITH hr_provinces AS (
	SELECT * FROM health_regions hr
	LEFT JOIN provinces p
	ON p.province_code = hr.fk_province_code
)
SELECT * FROM hr_provinces hp
LEFT JOIN regions r
ON hp.fk_region_id = r.id;