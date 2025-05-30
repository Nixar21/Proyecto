PGDMP  0    "                }            proyecto    17.5    17.5     )           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            *           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            +           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            ,           1262    24576    proyecto    DATABASE     {   CREATE DATABASE proyecto WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE proyecto;
                     postgres    false            �            1259    24585 
   credencial    TABLE     �   CREATE TABLE public.credencial (
    id_credencial integer NOT NULL,
    password_hash character varying(255),
    codigo_recuperacion character varying(100),
    fk_id_usuario integer
);
    DROP TABLE public.credencial;
       public         heap r       postgres    false            �            1259    24584    credencial_id_credencial_seq    SEQUENCE     �   CREATE SEQUENCE public.credencial_id_credencial_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.credencial_id_credencial_seq;
       public               postgres    false    220            -           0    0    credencial_id_credencial_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.credencial_id_credencial_seq OWNED BY public.credencial.id_credencial;
          public               postgres    false    219            �            1259    24578    usuario    TABLE     �   CREATE TABLE public.usuario (
    id_usuario integer NOT NULL,
    nombre character varying(100),
    apellido character varying(100),
    gmail character varying(255),
    dni character varying(20)
);
    DROP TABLE public.usuario;
       public         heap r       postgres    false            �            1259    24577    usuario_id_usuario_seq    SEQUENCE     �   CREATE SEQUENCE public.usuario_id_usuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.usuario_id_usuario_seq;
       public               postgres    false    218            .           0    0    usuario_id_usuario_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.usuario_id_usuario_seq OWNED BY public.usuario.id_usuario;
          public               postgres    false    217            �           2604    24588    credencial id_credencial    DEFAULT     �   ALTER TABLE ONLY public.credencial ALTER COLUMN id_credencial SET DEFAULT nextval('public.credencial_id_credencial_seq'::regclass);
 G   ALTER TABLE public.credencial ALTER COLUMN id_credencial DROP DEFAULT;
       public               postgres    false    220    219    220            �           2604    24581    usuario id_usuario    DEFAULT     x   ALTER TABLE ONLY public.usuario ALTER COLUMN id_usuario SET DEFAULT nextval('public.usuario_id_usuario_seq'::regclass);
 A   ALTER TABLE public.usuario ALTER COLUMN id_usuario DROP DEFAULT;
       public               postgres    false    218    217    218            &          0    24585 
   credencial 
   TABLE DATA           f   COPY public.credencial (id_credencial, password_hash, codigo_recuperacion, fk_id_usuario) FROM stdin;
    public               postgres    false    220   y       $          0    24578    usuario 
   TABLE DATA           K   COPY public.usuario (id_usuario, nombre, apellido, gmail, dni) FROM stdin;
    public               postgres    false    218   �       /           0    0    credencial_id_credencial_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.credencial_id_credencial_seq', 1, false);
          public               postgres    false    219            0           0    0    usuario_id_usuario_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.usuario_id_usuario_seq', 1, false);
          public               postgres    false    217            �           2606    24590    credencial credencial_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.credencial
    ADD CONSTRAINT credencial_pkey PRIMARY KEY (id_credencial);
 D   ALTER TABLE ONLY public.credencial DROP CONSTRAINT credencial_pkey;
       public                 postgres    false    220            �           2606    24583    usuario usuario_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public                 postgres    false    218            �           2606    24591    credencial fk_id_usuario    FK CONSTRAINT     �   ALTER TABLE ONLY public.credencial
    ADD CONSTRAINT fk_id_usuario FOREIGN KEY (fk_id_usuario) REFERENCES public.usuario(id_usuario) NOT VALID;
 B   ALTER TABLE ONLY public.credencial DROP CONSTRAINT fk_id_usuario;
       public               postgres    false    218    220    4750            &      x������ � �      $      x������ � �     