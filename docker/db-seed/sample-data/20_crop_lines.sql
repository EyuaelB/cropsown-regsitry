-- Crop Sown Registry — the seven crop lines for the records seeded in
-- 10_farmers_lands.sql. Per the updated ERD every line links straight to the
-- crop sown record (link_internal_record_id) and names its land by land_uuid.

INSERT INTO "public"."g2p_register_plannings" (
    "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
    "record_name","record_image_document_id","created_by","created_at","last_approved_at",
    "last_approved_by","search_text","record_status","record_status_reason",
    "land_uuid","season","commodity","crop_variety","crop_category","local_name","scientific_name",
    "plot_category","cropping_system","planned_date","planned_area","growth_duration_days",
    "expected_yield","seed_class","seed_source","planned_seed_qty","planned_fertilizer_type",
    "planned_fertilizer_qty","planned_labor","water_source","cluster_status"
) VALUES
('plan0001',NULL,'cs0001',NULL,'WHEAT MEHER 2.0',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00001 MEHER WHEAT KUBSA CEREALS ANNUAL_CROP MONO_CROPPING 2.0 IMPROVED COOPERATIVE UREA RAINFED CLUSTERED','ACTIVE',NULL,'11111111-1111-4111-8111-111111111111','MEHER','WHEAT','KUBSA','CEREALS','Sinde','Triticum aestivum','ANNUAL_CROP','MONO_CROPPING','2026-06-01',2.0,120,40.0,'IMPROVED','COOPERATIVE',150.0,'UREA',200.0,12,'RAINFED','CLUSTERED'),
('plan0002',NULL,'cs0001',NULL,'TEFF MEHER 1.0',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00002 MEHER TEFF QUNCHO CEREALS ANNUAL_CROP MONO_CROPPING 1.0 IMPROVED GOVERNMENT NPS RAINFED INDEPENDENT','ACTIVE',NULL,'22222222-2222-4222-8222-222222222222','MEHER','TEFF','QUNCHO','CEREALS','Teff','Eragrostis tef','ANNUAL_CROP','MONO_CROPPING','2026-06-15',1.0,110,12.0,'IMPROVED','GOVERNMENT',25.0,'NPS',100.0,8,'RAINFED','INDEPENDENT'),
('plan0003',NULL,'cs0002',NULL,'MAIZE MEHER 3.5',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','AM/04/01/007/00011 MEHER MAIZE BH_660 CEREALS ANNUAL_CROP MONO_CROPPING 3.5 IMPROVED MARKET NPSB IRRIGATION_SCHEME CLUSTERED','ACTIVE',NULL,'33333333-3333-4333-8333-333333333333','MEHER','MAIZE','BH_660','CEREALS','Bekolo','Zea mays','ANNUAL_CROP','MONO_CROPPING','2026-05-20',3.5,145,105.0,'IMPROVED','MARKET',87.5,'NPSB',350.0,20,'IRRIGATION_SCHEME','CLUSTERED')
ON CONFLICT ("internal_record_id") DO NOTHING;

INSERT INTO "public"."g2p_register_cultivations" (
    "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
    "record_name","record_image_document_id","created_by","created_at","last_approved_at",
    "last_approved_by","search_text","record_status","record_status_reason",
    "land_uuid","season","commodity","crop_variety","crop_category","land_prep_method",
    "cultivation_type","cropping_system","actual_planted_date","actual_crop_area",
    "actual_growth_duration_days","actual_seed_class","actual_seed_source","actual_seed_qty",
    "actual_fertilizer_type","actual_fertilizer_qty","water_source","remark"
) VALUES
('cult0001',NULL,'cs0001',NULL,'WHEAT TRACTOR_DISC_MOLDBOARD_PLOUGHING 2.0',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00001 MEHER WHEAT KUBSA CEREALS TRACTOR_DISC_MOLDBOARD_PLOUGHING TRACTOR_PLOUGHING 2.0 IMPROVED COOPERATIVE UREA RAINFED','ACTIVE',NULL,'11111111-1111-4111-8111-111111111111','MEHER','WHEAT','KUBSA','CEREALS','TRACTOR_DISC_MOLDBOARD_PLOUGHING','TRACTOR_PLOUGHING','MONO_CROPPING','2026-06-05',2.0,120,'IMPROVED','COOPERATIVE',148.0,'UREA',195.0,'RAINFED','Ploughed twice before sowing'),
('cult0002',NULL,'cs0001',NULL,'TEFF TRADITIONAL_MARESHA_PLOUGHING 1.0',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00002 MEHER TEFF QUNCHO CEREALS TRADITIONAL_MARESHA_PLOUGHING OXEN_TILLAGE 1.0 IMPROVED GOVERNMENT NPS RAINFED','ACTIVE',NULL,'22222222-2222-4222-8222-222222222222','MEHER','TEFF','QUNCHO','CEREALS','TRADITIONAL_MARESHA_PLOUGHING','OXEN_TILLAGE','MONO_CROPPING','2026-06-18',1.0,110,'IMPROVED','GOVERNMENT',24.0,'NPS',95.0,'RAINFED',NULL),
('cult0003',NULL,'cs0002',NULL,'MAIZE SHILSHALO 3.5',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','AM/04/01/007/00011 MEHER MAIZE BH_660 CEREALS SHILSHALO POWER_TILLER 3.5 IMPROVED MARKET NPSB IRRIGATION_SCHEME','ACTIVE',NULL,'33333333-3333-4333-8333-333333333333','MEHER','MAIZE','BH_660','CEREALS','SHILSHALO','POWER_TILLER','MONO_CROPPING','2026-05-25',3.5,145,'IMPROVED','MARKET',86.0,'NPSB',340.0,'IRRIGATION_SCHEME',NULL)
ON CONFLICT ("internal_record_id") DO NOTHING;

INSERT INTO "public"."g2p_register_sowings" (
    "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
    "record_name","record_image_document_id","created_by","created_at","last_approved_at",
    "last_approved_by","search_text","record_status","record_status_reason",
    "land_uuid","season","commodity","crop_variety","crop_category","sowing_status","area_sown",
    "sowing_date","seed_class","actual_seed_qty","fertilizer_type","fertilizer_qty",
    "cultivated_by","cluster_status","has_pest_disease"
) VALUES
('sow0001',NULL,'cs0001',NULL,'WHEAT MEHER 2.0',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00001 MEHER WHEAT KUBSA CEREALS FULLY_SOWN 2.0 IMPROVED UREA TRACTOR_PLOUGHING CLUSTERED','ACTIVE',NULL,'11111111-1111-4111-8111-111111111111','MEHER','WHEAT','KUBSA','CEREALS','FULLY_SOWN',2.0,'2026-06-20','IMPROVED',148.0,'UREA',195.0,'TRACTOR_PLOUGHING','CLUSTERED',TRUE),
('sow0002',NULL,'cs0001',NULL,'TEFF MEHER 0.8',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00002 MEHER TEFF QUNCHO CEREALS PARTIALLY_SOWN 0.8 IMPROVED NPS OXEN_TILLAGE INDEPENDENT','ACTIVE',NULL,'22222222-2222-4222-8222-222222222222','MEHER','TEFF','QUNCHO','CEREALS','PARTIALLY_SOWN',0.8,'2026-06-25','IMPROVED',20.0,'NPS',80.0,'OXEN_TILLAGE','INDEPENDENT',FALSE),
('sow0003',NULL,'cs0002',NULL,'MAIZE MEHER 3.5',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','AM/04/01/007/00011 MEHER MAIZE BH_660 CEREALS FULLY_SOWN 3.5 IMPROVED NPSB POWER_TILLER CLUSTERED','ACTIVE',NULL,'33333333-3333-4333-8333-333333333333','MEHER','MAIZE','BH_660','CEREALS','FULLY_SOWN',3.5,'2026-05-28','IMPROVED',86.0,'NPSB',340.0,'POWER_TILLER','CLUSTERED',FALSE)
ON CONFLICT ("internal_record_id") DO NOTHING;

INSERT INTO "public"."g2p_register_productions" (
    "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
    "record_name","record_image_document_id","created_by","created_at","last_approved_at",
    "last_approved_by","search_text","record_status","record_status_reason",
    "land_uuid","season","commodity","crop_variety","crop_category","growth_stage",
    "area_under_production","expected_yield","actual_yield","yield_per_ha",
    "land_utilization_rate","seed_productivity","fertilizer_efficiency","water_source","remark"
) VALUES
('prod0001',NULL,'cs0001',NULL,'WHEAT MEHER 38.0',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00001 MEHER WHEAT KUBSA CEREALS FLOWERING 2.0 40.0 38.0 RAINFED','ACTIVE',NULL,'11111111-1111-4111-8111-111111111111','MEHER','WHEAT','KUBSA','CEREALS','FLOWERING',2.0,40.0,38.0,19.0,80.0,0.2568,0.1949,'RAINFED',NULL),
('prod0002',NULL,'cs0002',NULL,'MAIZE MEHER 102.0',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','AM/04/01/007/00011 MEHER MAIZE BH_660 CEREALS MATURITY 3.5 105.0 102.0 IRRIGATION_SCHEME','ACTIVE',NULL,'33333333-3333-4333-8333-333333333333','MEHER','MAIZE','BH_660','CEREALS','MATURITY',3.5,105.0,102.0,29.14,93.33,1.1860,0.3000,'IRRIGATION_SCHEME',NULL)
ON CONFLICT ("internal_record_id") DO NOTHING;

INSERT INTO "public"."g2p_register_harvests" (
    "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
    "record_name","record_image_document_id","created_by","created_at","last_approved_at",
    "last_approved_by","search_text","record_status","record_status_reason",
    "land_uuid","commodity","crop_maturity_status","harvest_date","area_harvested",
    "qty_harvested","post_harvest_loss_pct","qty_stored","qty_sold","yield_per_ha","harvested_by"
) VALUES
('harv0001',NULL,'cs0002',NULL,'MAIZE 2026-10-20 102.0',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','AM/04/01/007/00011 MAIZE HARVESTED 2026-10-20 3.5 102.0 60.0 40.0 COMBINE_HARVESTER','ACTIVE',NULL,'33333333-3333-4333-8333-333333333333','MAIZE','HARVESTED','2026-10-20',3.5,102.0,4.5,60.0,40.0,29.14,'COMBINE_HARVESTER'),
('harv0002',NULL,'cs0001',NULL,'WHEAT READY_FOR_HARVEST',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00001 WHEAT READY_FOR_HARVEST','ACTIVE',NULL,'11111111-1111-4111-8111-111111111111','WHEAT','READY_FOR_HARVEST',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)
ON CONFLICT ("internal_record_id") DO NOTHING;

INSERT INTO "public"."g2p_register_infestations" (
    "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
    "record_name","record_image_document_id","created_by","created_at","last_approved_at",
    "last_approved_by","search_text","record_status","record_status_reason",
    "land_uuid","commodity","growth_stage","infestation_type","pest_name","weed_name",
    "disease_name","chemical_used","severity_level","estimated_damage_pct","observation_date",
    "geo_tagged_photo_document_id","action_taken"
) VALUES
('inf0001',NULL,'cs0001',NULL,'PEST MEDIUM 2026-08-12',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00001 WHEAT VEGETATIVE PEST ARMYWORM CYPERMETHRIN MEDIUM 2026-08-12','ACTIVE',NULL,'11111111-1111-4111-8111-111111111111','WHEAT','VEGETATIVE','PEST','ARMYWORM',NULL,NULL,'CYPERMETHRIN','MEDIUM',12.0,'2026-08-12',NULL,'Sprayed cypermethrin; DA follow-up scheduled'),
('inf0002',NULL,'cs0001',NULL,'WEED LOW 2026-07-30',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','OR/01/02/003/00001 WHEAT VEGETATIVE WEED BROADLEAF 2_4_D LOW 2026-07-30','ACTIVE',NULL,'11111111-1111-4111-8111-111111111111','WHEAT','VEGETATIVE','WEED',NULL,'BROADLEAF',NULL,'2_4_D','LOW',5.0,'2026-07-30',NULL,'Hand weeding plus selective herbicide')
ON CONFLICT ("internal_record_id") DO NOTHING;

INSERT INTO "public"."g2p_register_clusters" (
    "internal_record_id","functional_record_id","link_internal_record_id","link_foundational_id",
    "record_name","record_image_document_id","created_by","created_at","last_approved_at",
    "last_approved_by","search_text","record_status","record_status_reason",
    "cluster_name","cluster_status","agro_ecological_zone","season","commodity","sub_kebele",
    "cluster_area_hectare","number_of_smallholders","participant_farmers","collected_land",
    "collected_quintal","water_source","latitude","longitude","country_code"
) VALUES
('clu0001','CLR-000000000001','cs0001',NULL,'Gote 3 Wheat Cluster MEHER',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','CLR-000000000001 Gote 3 Wheat Cluster CLUSTERED WOINA_DEGA MEHER WHEAT Gote 3 120.0 RAINFED','ACTIVE',NULL,'Gote 3 Wheat Cluster','CLUSTERED','WOINA_DEGA','MEHER','WHEAT','Gote 3',120.0,85,80,110.0,3200.0,'RAINFED','9.0300','38.7400','ETH'),
('clu0002','CLR-000000000002','cs0002',NULL,'Gote 1 Maize Cluster MEHER',NULL,'seeder','2026-04-01 00:00:00','2026-04-01 00:00:00','seeder','CLR-000000000002 Gote 1 Maize Cluster CLUSTERED KOLLA MEHER MAIZE Gote 1 240.0 IRRIGATION_SCHEME','ACTIVE',NULL,'Gote 1 Maize Cluster','CLUSTERED','KOLLA','MEHER','MAIZE','Gote 1',240.0,150,141,232.0,7050.0,'IRRIGATION_SCHEME','8.5400','39.2700','ETH')
ON CONFLICT ("internal_record_id") DO NOTHING;
