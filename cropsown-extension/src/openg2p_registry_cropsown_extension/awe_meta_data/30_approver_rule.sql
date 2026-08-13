INSERT INTO "public"."approver_rule" (
    "id",
    "stage_id",
    "rule_type",
    "rule_value",
    "kind",
    "required",
    "created_at",
    "updated_at"
) VALUES
    ('0a1b2c3d-7183-44c5-8ff6-7c8d9eafb0c7', 'c3e5071a-3d4f-4081-acb2-3e4f5a6b7c83', 'user', '{"user_id": "alex.carter"}', 'approver', 'FALSE', NOW(), NOW()),
    ('1b2c3d4e-8294-45d6-90a7-8d9eafb0c1d8', 'd4f6182b-4e50-4192-bdc3-4f5a6b7c8d94', 'user', '{"user_id": "nina.patel"}', 'approver', 'FALSE', NOW(), NOW()),
    ('2c3d4e5f-93a5-46e7-a1b8-9eafb0c1d2e9', 'e507293c-5f61-42a3-ced4-5a6b7c8d9ea5', 'user', '{"user_id": "alex.carter"}', 'approver', 'FALSE', NOW(), NOW()),
    ('3d4e5f60-a4b6-47f8-b2c9-afb0c1d2e3fa', 'f618304d-6072-43b4-dfe5-6b7c8d9eafb6', 'user', '{"user_id": "nina.patel"}', 'approver', 'FALSE', NOW(), NOW())
ON CONFLICT ("id") DO NOTHING;
