-- Crop Sown Registry — demo record photos.
--
-- The profile widget on Farmer Identity resolves record_image_document_id
-- through /documents/get_documents, which reads the object named by
-- document_store_id from the `documents` bucket. So a photo needs three things:
-- the object in MinIO (images/ alongside this file, copied in by db-seed), a
-- row here, and the id on the record.
--
-- These are flat placeholder portraits in the ATI palette, not photographs.

INSERT INTO "public"."g2p_registry_documents"
    ("document_id","document_store_id","bucket","source_filename","created_by","created_at")
VALUES
('9a1e5c70-1111-4a51-9c31-0b7d5e3a1001','farmer_01.png','documents','farmer_01.png','seeder','2026-04-01 00:00:00'),
('9a1e5c70-2222-4a51-9c31-0b7d5e3a1002','farmer_02.png','documents','farmer_02.png','seeder','2026-04-01 00:00:00'),
('9a1e5c70-3333-4a51-9c31-0b7d5e3a1003','farmer_03.png','documents','farmer_03.png','seeder','2026-04-01 00:00:00')
ON CONFLICT ("document_id") DO NOTHING;

UPDATE "public"."g2p_register_crop_sowns"
   SET "record_image_document_id" = '/images/records/farmer_01.png'
 WHERE "internal_record_id" = 'cs0001';
UPDATE "public"."g2p_register_crop_sowns"
   SET "record_image_document_id" = '/images/records/farmer_02.png'
 WHERE "internal_record_id" = 'cs0002';
UPDATE "public"."g2p_register_crop_sowns"
   SET "record_image_document_id" = '/images/records/farmer_03.png'
 WHERE "internal_record_id" = 'cs0003';
