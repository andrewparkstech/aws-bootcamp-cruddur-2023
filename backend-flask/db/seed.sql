-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Andrew Brown','redacted+email@gmail.com' , 'andrewbrown' ,'3db080dd-716a-40d4-80f4-97d85ea16435'),
  ('Andrew Parks','redacted+email@gmail.com' , 'aparks' ,'96e9596a-fa80-4e15-90f3-0191e76a51b0'),
  ('Londo Mollari','lmollari@centari.com' ,'londo' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )