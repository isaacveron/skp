PGDMP     4    7    
            s            skp    9.1.13    9.1.13 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           1262    40404    skp    DATABASE     u   CREATE DATABASE skp WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'es_PY.UTF-8' LC_CTYPE = 'es_PY.UTF-8';
    DROP DATABASE skp;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    5            �           0    0    public    ACL     �   REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;
                  postgres    false    5            �            3079    11679    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            �           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    198            �            1259    40438 
   auth_group    TABLE     �   CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    "Fecha" timestamp with time zone,
    "Usuario_id" integer
);
    DROP TABLE public.auth_group;
       public         root    false    5            �            1259    40436    auth_group_id_seq    SEQUENCE     s   CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       root    false    5    168            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;
            public       root    false    167            �            1259    40448    auth_group_permissions    TABLE     �   CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         root    false    5            �            1259    40446    auth_group_permissions_id_seq    SEQUENCE        CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       root    false    5    170            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;
            public       root    false    169            �            1259    40428    auth_permission    TABLE     �   CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         root    false    5            �            1259    40426    auth_permission_id_seq    SEQUENCE     x   CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       root    false    5    166            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;
            public       root    false    165            �            1259    40458 	   auth_user    TABLE     ^  CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    direccion text,
    observacion text,
    telefono integer,
    CONSTRAINT auth_user_telefono_check CHECK ((telefono >= 0))
);
    DROP TABLE public.auth_user;
       public         root    false    1906    5            �            1259    40468    auth_user_groups    TABLE     x   CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         root    false    5            �            1259    40466    auth_user_groups_id_seq    SEQUENCE     y   CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       root    false    174    5            �           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;
            public       root    false    173            �            1259    40456    auth_user_id_seq    SEQUENCE     r   CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       root    false    172    5            �           0    0    auth_user_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;
            public       root    false    171            �            1259    40478    auth_user_user_permissions    TABLE     �   CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         root    false    5            �            1259    40476 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       root    false    176    5            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;
            public       root    false    175            �            1259    40532    django_admin_log    TABLE     �  CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         root    false    1910    5            �            1259    40530    django_admin_log_id_seq    SEQUENCE     y   CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       root    false    178    5            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;
            public       root    false    177            �            1259    40418    django_content_type    TABLE     �   CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         root    false    5            �            1259    40416    django_content_type_id_seq    SEQUENCE     |   CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       root    false    5    164            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;
            public       root    false    163            �            1259    40407    django_migrations    TABLE     �   CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         root    false    5            �            1259    40405    django_migrations_id_seq    SEQUENCE     z   CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       root    false    5    162            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;
            public       root    false    161            �            1259    40740    django_session    TABLE     �   CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         root    false    5            �            1259    40579    flujos_actividad    TABLE     �   CREATE TABLE flujos_actividad (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Orden" integer,
    "idTabla" integer
);
 $   DROP TABLE public.flujos_actividad;
       public         root    false    5            �            1259    40577    flujos_actividad_id_seq    SEQUENCE     y   CREATE SEQUENCE flujos_actividad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.flujos_actividad_id_seq;
       public       root    false    5    180            �           0    0    flujos_actividad_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE flujos_actividad_id_seq OWNED BY flujos_actividad.id;
            public       root    false    179            �            1259    40589    flujos_flujo    TABLE     �   CREATE TABLE flujos_flujo (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Estado" character varying(15) NOT NULL,
    "Descripcion" text,
    "Fecha_creacion" timestamp with time zone,
    "Usuario_creador_id" integer
);
     DROP TABLE public.flujos_flujo;
       public         root    false    5            �            1259    40602    flujos_flujo_Actividades    TABLE     �   CREATE TABLE "flujos_flujo_Actividades" (
    id integer NOT NULL,
    flujo_id integer NOT NULL,
    actividad_id integer NOT NULL
);
 .   DROP TABLE public."flujos_flujo_Actividades";
       public         root    false    5            �            1259    40600    flujos_flujo_Actividades_id_seq    SEQUENCE     �   CREATE SEQUENCE "flujos_flujo_Actividades_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."flujos_flujo_Actividades_id_seq";
       public       root    false    5    184            �           0    0    flujos_flujo_Actividades_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE "flujos_flujo_Actividades_id_seq" OWNED BY "flujos_flujo_Actividades".id;
            public       root    false    183            �            1259    40587    flujos_flujo_id_seq    SEQUENCE     u   CREATE SEQUENCE flujos_flujo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.flujos_flujo_id_seq;
       public       root    false    5    182            �           0    0    flujos_flujo_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE flujos_flujo_id_seq OWNED BY flujos_flujo.id;
            public       root    false    181            �            1259    40662    proyectos_proyecto    TABLE     |  CREATE TABLE proyectos_proyecto (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Descripcion" text,
    "Fecha_inicio" date,
    "Fecha_finalizacion" date,
    "Cliente" character varying(30),
    "Estado" character varying(15) NOT NULL,
    "Scrum_Master_id" integer,
    "Fecha_creacion" timestamp with time zone,
    "Usuario_creador_id" integer
);
 &   DROP TABLE public.proyectos_proyecto;
       public         root    false    5            �            1259    40675     proyectos_proyecto_Grupo_trabajo    TABLE     �   CREATE TABLE "proyectos_proyecto_Grupo_trabajo" (
    id integer NOT NULL,
    proyecto_id integer NOT NULL,
    user_id integer NOT NULL
);
 6   DROP TABLE public."proyectos_proyecto_Grupo_trabajo";
       public         root    false    5            �            1259    40673 '   proyectos_proyecto_Grupo_trabajo_id_seq    SEQUENCE     �   CREATE SEQUENCE "proyectos_proyecto_Grupo_trabajo_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 @   DROP SEQUENCE public."proyectos_proyecto_Grupo_trabajo_id_seq";
       public       root    false    5    188            �           0    0 '   proyectos_proyecto_Grupo_trabajo_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE "proyectos_proyecto_Grupo_trabajo_id_seq" OWNED BY "proyectos_proyecto_Grupo_trabajo".id;
            public       root    false    187            �            1259    40660    proyectos_proyecto_id_seq    SEQUENCE     {   CREATE SEQUENCE proyectos_proyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.proyectos_proyecto_id_seq;
       public       root    false    186    5            �           0    0    proyectos_proyecto_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE proyectos_proyecto_id_seq OWNED BY proyectos_proyecto.id;
            public       root    false    185            �            1259    40781    sprint_sprint    TABLE     �  CREATE TABLE sprint_sprint (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Descripcion" text,
    "Fecha_inicio" date,
    "Fecha_finalizacion" date,
    "Cliente" character varying(30),
    "Estado" character varying(15) NOT NULL,
    "Fecha_creacion" timestamp with time zone,
    "Usuario_creador_id" integer,
    "Proyecto_asignado_id" integer,
    "Duracion" integer,
    is_active boolean NOT NULL,
    CONSTRAINT "sprint_sprint_Duracion_check" CHECK (("Duracion" >= 0))
);
 !   DROP TABLE public.sprint_sprint;
       public         root    false    1923    5            �            1259    40823    sprint_sprint_UserStorys    TABLE     �   CREATE TABLE "sprint_sprint_UserStorys" (
    id integer NOT NULL,
    sprint_id integer NOT NULL,
    userstory_id integer NOT NULL
);
 .   DROP TABLE public."sprint_sprint_UserStorys";
       public         root    false    5            �            1259    40821    sprint_sprint_UserStorys_id_seq    SEQUENCE     �   CREATE SEQUENCE "sprint_sprint_UserStorys_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."sprint_sprint_UserStorys_id_seq";
       public       root    false    195    5            �           0    0    sprint_sprint_UserStorys_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE "sprint_sprint_UserStorys_id_seq" OWNED BY "sprint_sprint_UserStorys".id;
            public       root    false    194            �            1259    40779    sprint_sprint_id_seq    SEQUENCE     v   CREATE SEQUENCE sprint_sprint_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.sprint_sprint_id_seq;
       public       root    false    193    5            �           0    0    sprint_sprint_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE sprint_sprint_id_seq OWNED BY sprint_sprint.id;
            public       root    false    192            �            1259    40888    userstory_cargarhoras    TABLE     �   CREATE TABLE userstory_cargarhoras (
    id integer NOT NULL,
    "Horas" integer,
    "Descripcion" text,
    "US_asignado_id" integer,
    CONSTRAINT "userstory_cargarhoras_Horas_check" CHECK (("Horas" >= 0))
);
 )   DROP TABLE public.userstory_cargarhoras;
       public         root    false    1926    5            �            1259    40886    userstory_cargarhoras_id_seq    SEQUENCE     ~   CREATE SEQUENCE userstory_cargarhoras_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.userstory_cargarhoras_id_seq;
       public       root    false    5    197            �           0    0    userstory_cargarhoras_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE userstory_cargarhoras_id_seq OWNED BY userstory_cargarhoras.id;
            public       root    false    196            �            1259    40752    userstory_userstory    TABLE     �  CREATE TABLE userstory_userstory (
    id integer NOT NULL,
    "Nombre" character varying(30) NOT NULL,
    "Descripcion" text,
    "Valor_tecnico" integer,
    "Valor_de_negocio" integer,
    "Size" integer,
    "Estado" character varying(15) NOT NULL,
    "Fecha_creacion" timestamp with time zone,
    "Usuario_asignado_id" integer,
    "Usuario_creador_id" integer,
    "Proyecto_asignado_id" integer,
    is_active boolean NOT NULL,
    "Sub_version" integer,
    "Version" integer,
    CONSTRAINT "userstory_userstory_Size_check" CHECK (("Size" >= 0)),
    CONSTRAINT "userstory_userstory_Sub_version_check" CHECK (("Sub_version" >= 0)),
    CONSTRAINT "userstory_userstory_Valor_de_negocio_check" CHECK (("Valor_de_negocio" >= 0)),
    CONSTRAINT "userstory_userstory_Valor_tecnico_check" CHECK (("Valor_tecnico" >= 0)),
    CONSTRAINT "userstory_userstory_Version_check" CHECK (("Version" >= 0))
);
 '   DROP TABLE public.userstory_userstory;
       public         root    false    1917    1918    1919    1920    1921    5            �            1259    40750    userstory_userstory_id_seq    SEQUENCE     |   CREATE SEQUENCE userstory_userstory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.userstory_userstory_id_seq;
       public       root    false    191    5            �           0    0    userstory_userstory_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE userstory_userstory_id_seq OWNED BY userstory_userstory.id;
            public       root    false    190            o           2604    40441    id    DEFAULT     `   ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       root    false    167    168    168            p           2604    40451    id    DEFAULT     x   ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       root    false    170    169    170            n           2604    40431    id    DEFAULT     j   ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       root    false    165    166    166            q           2604    40461    id    DEFAULT     ^   ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       root    false    171    172    172            s           2604    40471    id    DEFAULT     l   ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       root    false    174    173    174            t           2604    40481    id    DEFAULT     �   ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       root    false    176    175    176            u           2604    40535    id    DEFAULT     l   ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       root    false    177    178    178            m           2604    40421    id    DEFAULT     r   ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       root    false    163    164    164            l           2604    40410    id    DEFAULT     n   ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       root    false    161    162    162            w           2604    40582    id    DEFAULT     l   ALTER TABLE ONLY flujos_actividad ALTER COLUMN id SET DEFAULT nextval('flujos_actividad_id_seq'::regclass);
 B   ALTER TABLE public.flujos_actividad ALTER COLUMN id DROP DEFAULT;
       public       root    false    180    179    180            x           2604    40592    id    DEFAULT     d   ALTER TABLE ONLY flujos_flujo ALTER COLUMN id SET DEFAULT nextval('flujos_flujo_id_seq'::regclass);
 >   ALTER TABLE public.flujos_flujo ALTER COLUMN id DROP DEFAULT;
       public       root    false    182    181    182            y           2604    40605    id    DEFAULT     �   ALTER TABLE ONLY "flujos_flujo_Actividades" ALTER COLUMN id SET DEFAULT nextval('"flujos_flujo_Actividades_id_seq"'::regclass);
 L   ALTER TABLE public."flujos_flujo_Actividades" ALTER COLUMN id DROP DEFAULT;
       public       root    false    184    183    184            z           2604    40665    id    DEFAULT     p   ALTER TABLE ONLY proyectos_proyecto ALTER COLUMN id SET DEFAULT nextval('proyectos_proyecto_id_seq'::regclass);
 D   ALTER TABLE public.proyectos_proyecto ALTER COLUMN id DROP DEFAULT;
       public       root    false    185    186    186            {           2604    40678    id    DEFAULT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo" ALTER COLUMN id SET DEFAULT nextval('"proyectos_proyecto_Grupo_trabajo_id_seq"'::regclass);
 T   ALTER TABLE public."proyectos_proyecto_Grupo_trabajo" ALTER COLUMN id DROP DEFAULT;
       public       root    false    187    188    188            �           2604    40784    id    DEFAULT     f   ALTER TABLE ONLY sprint_sprint ALTER COLUMN id SET DEFAULT nextval('sprint_sprint_id_seq'::regclass);
 ?   ALTER TABLE public.sprint_sprint ALTER COLUMN id DROP DEFAULT;
       public       root    false    193    192    193            �           2604    40826    id    DEFAULT     �   ALTER TABLE ONLY "sprint_sprint_UserStorys" ALTER COLUMN id SET DEFAULT nextval('"sprint_sprint_UserStorys_id_seq"'::regclass);
 L   ALTER TABLE public."sprint_sprint_UserStorys" ALTER COLUMN id DROP DEFAULT;
       public       root    false    194    195    195            �           2604    40891    id    DEFAULT     v   ALTER TABLE ONLY userstory_cargarhoras ALTER COLUMN id SET DEFAULT nextval('userstory_cargarhoras_id_seq'::regclass);
 G   ALTER TABLE public.userstory_cargarhoras ALTER COLUMN id DROP DEFAULT;
       public       root    false    196    197    197            |           2604    40755    id    DEFAULT     r   ALTER TABLE ONLY userstory_userstory ALTER COLUMN id SET DEFAULT nextval('userstory_userstory_id_seq'::regclass);
 E   ALTER TABLE public.userstory_userstory ALTER COLUMN id DROP DEFAULT;
       public       root    false    191    190    191            p          0    40438 
   auth_group 
   TABLE DATA               >   COPY auth_group (id, name, "Fecha", "Usuario_id") FROM stdin;
    public       root    false    168    2190   M      �           0    0    auth_group_id_seq    SEQUENCE SET     8   SELECT pg_catalog.setval('auth_group_id_seq', 1, true);
            public       root    false    167            r          0    40448    auth_group_permissions 
   TABLE DATA               F   COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       root    false    170    2190   �      �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('auth_group_permissions_id_seq', 165, true);
            public       root    false    169            n          0    40428    auth_permission 
   TABLE DATA               G   COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       root    false    166    2190   +      �           0    0    auth_permission_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('auth_permission_id_seq', 36, true);
            public       root    false    165            t          0    40458 	   auth_user 
   TABLE DATA               �   COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, direccion, observacion, telefono) FROM stdin;
    public       root    false    172    2190   �      v          0    40468    auth_user_groups 
   TABLE DATA               :   COPY auth_user_groups (id, user_id, group_id) FROM stdin;
    public       root    false    174    2190   c      �           0    0    auth_user_groups_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, true);
            public       root    false    173            �           0    0    auth_user_id_seq    SEQUENCE SET     7   SELECT pg_catalog.setval('auth_user_id_seq', 3, true);
            public       root    false    171            x          0    40478    auth_user_user_permissions 
   TABLE DATA               I   COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       root    false    176    2190   �      �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);
            public       root    false    175            z          0    40532    django_admin_log 
   TABLE DATA               �   COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       root    false    178    2190   �      �           0    0    django_admin_log_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);
            public       root    false    177            l          0    40418    django_content_type 
   TABLE DATA               B   COPY django_content_type (id, name, app_label, model) FROM stdin;
    public       root    false    164    2190   �      �           0    0    django_content_type_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('django_content_type_id_seq', 12, true);
            public       root    false    163            j          0    40407    django_migrations 
   TABLE DATA               <   COPY django_migrations (id, app, name, applied) FROM stdin;
    public       root    false    162    2190   }      �           0    0    django_migrations_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('django_migrations_id_seq', 38, true);
            public       root    false    161            �          0    40740    django_session 
   TABLE DATA               I   COPY django_session (session_key, session_data, expire_date) FROM stdin;
    public       root    false    189    2190   @      |          0    40579    flujos_actividad 
   TABLE DATA               E   COPY flujos_actividad (id, "Nombre", "Orden", "idTabla") FROM stdin;
    public       root    false    180    2190   Z!      �           0    0    flujos_actividad_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('flujos_actividad_id_seq', 3, true);
            public       root    false    179            ~          0    40589    flujos_flujo 
   TABLE DATA               n   COPY flujos_flujo (id, "Nombre", "Estado", "Descripcion", "Fecha_creacion", "Usuario_creador_id") FROM stdin;
    public       root    false    182    2190   �!      �          0    40602    flujos_flujo_Actividades 
   TABLE DATA               I   COPY "flujos_flujo_Actividades" (id, flujo_id, actividad_id) FROM stdin;
    public       root    false    184    2190   �!      �           0    0    flujos_flujo_Actividades_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('"flujos_flujo_Actividades_id_seq"', 3, true);
            public       root    false    183            �           0    0    flujos_flujo_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('flujos_flujo_id_seq', 1, true);
            public       root    false    181            �          0    40662    proyectos_proyecto 
   TABLE DATA               �   COPY proyectos_proyecto (id, "Nombre", "Descripcion", "Fecha_inicio", "Fecha_finalizacion", "Cliente", "Estado", "Scrum_Master_id", "Fecha_creacion", "Usuario_creador_id") FROM stdin;
    public       root    false    186    2190   	"      �          0    40675     proyectos_proyecto_Grupo_trabajo 
   TABLE DATA               O   COPY "proyectos_proyecto_Grupo_trabajo" (id, proyecto_id, user_id) FROM stdin;
    public       root    false    188    2190   }"      �           0    0 '   proyectos_proyecto_Grupo_trabajo_id_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('"proyectos_proyecto_Grupo_trabajo_id_seq"', 15, true);
            public       root    false    187            �           0    0    proyectos_proyecto_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('proyectos_proyecto_id_seq', 4, true);
            public       root    false    185            �          0    40781    sprint_sprint 
   TABLE DATA               �   COPY sprint_sprint (id, "Nombre", "Descripcion", "Fecha_inicio", "Fecha_finalizacion", "Cliente", "Estado", "Fecha_creacion", "Usuario_creador_id", "Proyecto_asignado_id", "Duracion", is_active) FROM stdin;
    public       root    false    193    2190   �"      �          0    40823    sprint_sprint_UserStorys 
   TABLE DATA               J   COPY "sprint_sprint_UserStorys" (id, sprint_id, userstory_id) FROM stdin;
    public       root    false    195    2190   S#      �           0    0    sprint_sprint_UserStorys_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('"sprint_sprint_UserStorys_id_seq"', 101, true);
            public       root    false    194            �           0    0    sprint_sprint_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('sprint_sprint_id_seq', 29, true);
            public       root    false    192            �          0    40888    userstory_cargarhoras 
   TABLE DATA               V   COPY userstory_cargarhoras (id, "Horas", "Descripcion", "US_asignado_id") FROM stdin;
    public       root    false    197    2190   �#      �           0    0    userstory_cargarhoras_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('userstory_cargarhoras_id_seq', 17, true);
            public       root    false    196            �          0    40752    userstory_userstory 
   TABLE DATA               �   COPY userstory_userstory (id, "Nombre", "Descripcion", "Valor_tecnico", "Valor_de_negocio", "Size", "Estado", "Fecha_creacion", "Usuario_asignado_id", "Usuario_creador_id", "Proyecto_asignado_id", is_active, "Sub_version", "Version") FROM stdin;
    public       root    false    191    2190   �#      �           0    0    userstory_userstory_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('userstory_userstory_id_seq', 34, true);
            public       root    false    190            �           2606    40445    auth_group_name_key 
   CONSTRAINT     R   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         root    false    168    168    2191            �           2606    40455 1   auth_group_permissions_group_id_permission_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);
 r   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_key;
       public         root    false    170    170    170    2191            �           2606    40453    auth_group_permissions_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         root    false    170    170    2191            �           2606    40443    auth_group_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         root    false    168    168    2191            �           2606    40435 ,   auth_permission_content_type_id_codename_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);
 f   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_key;
       public         root    false    166    166    166    2191            �           2606    40433    auth_permission_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         root    false    166    166    2191            �           2606    40473    auth_user_groups_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         root    false    174    174    2191            �           2606    40475 %   auth_user_groups_user_id_group_id_key 
   CONSTRAINT     w   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);
 `   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_key;
       public         root    false    174    174    174    2191            �           2606    40463    auth_user_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         root    false    172    172    2191            �           2606    40483    auth_user_user_permissions_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         root    false    176    176    2191            �           2606    40485 4   auth_user_user_permissions_user_id_permission_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);
 y   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_key;
       public         root    false    176    176    176    2191            �           2606    40465    auth_user_username_key 
   CONSTRAINT     X   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         root    false    172    172    2191            �           2606    40541    django_admin_log_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         root    false    178    178    2191            �           2606    40425 3   django_content_type_app_label_45f3b1d93ec8c61c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);
 q   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq;
       public         root    false    164    164    164    2191            �           2606    40423    django_content_type_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         root    false    164    164    2191            �           2606    40415    django_migrations_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         root    false    162    162    2191            �           2606    40747    django_session_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         root    false    189    189    2191            �           2606    40584    flujos_actividad_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY flujos_actividad
    ADD CONSTRAINT flujos_actividad_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.flujos_actividad DROP CONSTRAINT flujos_actividad_pkey;
       public         root    false    180    180    2191            �           2606    40609 2   flujos_flujo_Actividades_flujo_id_actividad_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "flujos_flujo_Actividades"
    ADD CONSTRAINT "flujos_flujo_Actividades_flujo_id_actividad_id_key" UNIQUE (flujo_id, actividad_id);
 y   ALTER TABLE ONLY public."flujos_flujo_Actividades" DROP CONSTRAINT "flujos_flujo_Actividades_flujo_id_actividad_id_key";
       public         root    false    184    184    184    2191            �           2606    40607    flujos_flujo_Actividades_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY "flujos_flujo_Actividades"
    ADD CONSTRAINT "flujos_flujo_Actividades_pkey" PRIMARY KEY (id);
 d   ALTER TABLE ONLY public."flujos_flujo_Actividades" DROP CONSTRAINT "flujos_flujo_Actividades_pkey";
       public         root    false    184    184    2191            �           2606    40599    flujos_flujo_Nombre_key 
   CONSTRAINT     ^   ALTER TABLE ONLY flujos_flujo
    ADD CONSTRAINT "flujos_flujo_Nombre_key" UNIQUE ("Nombre");
 P   ALTER TABLE ONLY public.flujos_flujo DROP CONSTRAINT "flujos_flujo_Nombre_key";
       public         root    false    182    182    2191            �           2606    40597    flujos_flujo_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY flujos_flujo
    ADD CONSTRAINT flujos_flujo_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.flujos_flujo DROP CONSTRAINT flujos_flujo_pkey;
       public         root    false    182    182    2191            �           2606    40680 %   proyectos_proyecto_Grupo_trabajo_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo"
    ADD CONSTRAINT "proyectos_proyecto_Grupo_trabajo_pkey" PRIMARY KEY (id);
 t   ALTER TABLE ONLY public."proyectos_proyecto_Grupo_trabajo" DROP CONSTRAINT "proyectos_proyecto_Grupo_trabajo_pkey";
       public         root    false    188    188    2191            �           2606    40682 8   proyectos_proyecto_Grupo_trabajo_proyecto_id_user_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo"
    ADD CONSTRAINT "proyectos_proyecto_Grupo_trabajo_proyecto_id_user_id_key" UNIQUE (proyecto_id, user_id);
 �   ALTER TABLE ONLY public."proyectos_proyecto_Grupo_trabajo" DROP CONSTRAINT "proyectos_proyecto_Grupo_trabajo_proyecto_id_user_id_key";
       public         root    false    188    188    188    2191            �           2606    40672    proyectos_proyecto_Nombre_key 
   CONSTRAINT     j   ALTER TABLE ONLY proyectos_proyecto
    ADD CONSTRAINT "proyectos_proyecto_Nombre_key" UNIQUE ("Nombre");
 \   ALTER TABLE ONLY public.proyectos_proyecto DROP CONSTRAINT "proyectos_proyecto_Nombre_key";
       public         root    false    186    186    2191            �           2606    40670    proyectos_proyecto_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY proyectos_proyecto
    ADD CONSTRAINT proyectos_proyecto_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.proyectos_proyecto DROP CONSTRAINT proyectos_proyecto_pkey;
       public         root    false    186    186    2191            �           2606    40791    sprint_sprint_Nombre_key 
   CONSTRAINT     `   ALTER TABLE ONLY sprint_sprint
    ADD CONSTRAINT "sprint_sprint_Nombre_key" UNIQUE ("Nombre");
 R   ALTER TABLE ONLY public.sprint_sprint DROP CONSTRAINT "sprint_sprint_Nombre_key";
       public         root    false    193    193    2191            �           2606    40828    sprint_sprint_UserStorys_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY "sprint_sprint_UserStorys"
    ADD CONSTRAINT "sprint_sprint_UserStorys_pkey" PRIMARY KEY (id);
 d   ALTER TABLE ONLY public."sprint_sprint_UserStorys" DROP CONSTRAINT "sprint_sprint_UserStorys_pkey";
       public         root    false    195    195    2191            �           2606    40830 3   sprint_sprint_UserStorys_sprint_id_userstory_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY "sprint_sprint_UserStorys"
    ADD CONSTRAINT "sprint_sprint_UserStorys_sprint_id_userstory_id_key" UNIQUE (sprint_id, userstory_id);
 z   ALTER TABLE ONLY public."sprint_sprint_UserStorys" DROP CONSTRAINT "sprint_sprint_UserStorys_sprint_id_userstory_id_key";
       public         root    false    195    195    195    2191            �           2606    40789    sprint_sprint_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY sprint_sprint
    ADD CONSTRAINT sprint_sprint_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.sprint_sprint DROP CONSTRAINT sprint_sprint_pkey;
       public         root    false    193    193    2191            �           2606    40897    userstory_cargarhoras_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY userstory_cargarhoras
    ADD CONSTRAINT userstory_cargarhoras_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.userstory_cargarhoras DROP CONSTRAINT userstory_cargarhoras_pkey;
       public         root    false    197    197    2191            �           2606    40765    userstory_userstory_Nombre_key 
   CONSTRAINT     l   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT "userstory_userstory_Nombre_key" UNIQUE ("Nombre");
 ^   ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT "userstory_userstory_Nombre_key";
       public         root    false    191    191    2191            �           2606    40763    userstory_userstory_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT userstory_userstory_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT userstory_userstory_pkey;
       public         root    false    191    191    2191            �           1259    40571    auth_group_ae6be32e    INDEX     K   CREATE INDEX auth_group_ae6be32e ON auth_group USING btree ("Usuario_id");
 '   DROP INDEX public.auth_group_ae6be32e;
       public         root    false    168    2191            �           1259    40492 %   auth_group_name_253ae2a6331666e8_like    INDEX     i   CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);
 9   DROP INDEX public.auth_group_name_253ae2a6331666e8_like;
       public         root    false    168    2191            �           1259    40503    auth_group_permissions_0e939a4f    INDEX     _   CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);
 3   DROP INDEX public.auth_group_permissions_0e939a4f;
       public         root    false    170    2191            �           1259    40504    auth_group_permissions_8373b171    INDEX     d   CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);
 3   DROP INDEX public.auth_group_permissions_8373b171;
       public         root    false    170    2191            �           1259    40491    auth_permission_417f1b1c    INDEX     X   CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);
 ,   DROP INDEX public.auth_permission_417f1b1c;
       public         root    false    166    2191            �           1259    40517    auth_user_groups_0e939a4f    INDEX     S   CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);
 -   DROP INDEX public.auth_user_groups_0e939a4f;
       public         root    false    174    2191            �           1259    40516    auth_user_groups_e8701ad4    INDEX     R   CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);
 -   DROP INDEX public.auth_user_groups_e8701ad4;
       public         root    false    174    2191            �           1259    40529 #   auth_user_user_permissions_8373b171    INDEX     l   CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);
 7   DROP INDEX public.auth_user_user_permissions_8373b171;
       public         root    false    176    2191            �           1259    40528 #   auth_user_user_permissions_e8701ad4    INDEX     f   CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);
 7   DROP INDEX public.auth_user_user_permissions_e8701ad4;
       public         root    false    176    2191            �           1259    40505 (   auth_user_username_51b3b110094b8aae_like    INDEX     o   CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);
 <   DROP INDEX public.auth_user_username_51b3b110094b8aae_like;
       public         root    false    172    2191            �           1259    40552    django_admin_log_417f1b1c    INDEX     Z   CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);
 -   DROP INDEX public.django_admin_log_417f1b1c;
       public         root    false    178    2191            �           1259    40553    django_admin_log_e8701ad4    INDEX     R   CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);
 -   DROP INDEX public.django_admin_log_e8701ad4;
       public         root    false    178    2191            �           1259    40748    django_session_de54fa62    INDEX     R   CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);
 +   DROP INDEX public.django_session_de54fa62;
       public         root    false    189    2191            �           1259    40749 0   django_session_session_key_461cfeaa630ca218_like    INDEX        CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);
 D   DROP INDEX public.django_session_session_key_461cfeaa630ca218_like;
       public         root    false    189    2191            �           1259    40610 -   flujos_actividad_Nombre_42c266ccd5b5837d_like    INDEX     }   CREATE INDEX "flujos_actividad_Nombre_42c266ccd5b5837d_like" ON flujos_actividad USING btree ("Nombre" varchar_pattern_ops);
 C   DROP INDEX public."flujos_actividad_Nombre_42c266ccd5b5837d_like";
       public         root    false    180    2191            �           1259    40616    flujos_flujo_56ac0855    INDEX     W   CREATE INDEX flujos_flujo_56ac0855 ON flujos_flujo USING btree ("Usuario_creador_id");
 )   DROP INDEX public.flujos_flujo_56ac0855;
       public         root    false    182    2191            �           1259    40629 !   flujos_flujo_Actividades_6f919ae9    INDEX     k   CREATE INDEX "flujos_flujo_Actividades_6f919ae9" ON "flujos_flujo_Actividades" USING btree (actividad_id);
 7   DROP INDEX public."flujos_flujo_Actividades_6f919ae9";
       public         root    false    184    2191            �           1259    40628 !   flujos_flujo_Actividades_bd1d5624    INDEX     g   CREATE INDEX "flujos_flujo_Actividades_bd1d5624" ON "flujos_flujo_Actividades" USING btree (flujo_id);
 7   DROP INDEX public."flujos_flujo_Actividades_bd1d5624";
       public         root    false    184    2191            �           1259    40617 (   flujos_flujo_Nombre_80ac4eefc469076_like    INDEX     t   CREATE INDEX "flujos_flujo_Nombre_80ac4eefc469076_like" ON flujos_flujo USING btree ("Nombre" varchar_pattern_ops);
 >   DROP INDEX public."flujos_flujo_Nombre_80ac4eefc469076_like";
       public         root    false    182    2191            �           1259    40702    proyectos_proyecto_56ac0855    INDEX     c   CREATE INDEX proyectos_proyecto_56ac0855 ON proyectos_proyecto USING btree ("Usuario_creador_id");
 /   DROP INDEX public.proyectos_proyecto_56ac0855;
       public         root    false    186    2191            �           1259    40701 )   proyectos_proyecto_Grupo_trabajo_e8701ad4    INDEX     v   CREATE INDEX "proyectos_proyecto_Grupo_trabajo_e8701ad4" ON "proyectos_proyecto_Grupo_trabajo" USING btree (user_id);
 ?   DROP INDEX public."proyectos_proyecto_Grupo_trabajo_e8701ad4";
       public         root    false    188    2191            �           1259    40700 )   proyectos_proyecto_Grupo_trabajo_f543c3f9    INDEX     z   CREATE INDEX "proyectos_proyecto_Grupo_trabajo_f543c3f9" ON "proyectos_proyecto_Grupo_trabajo" USING btree (proyecto_id);
 ?   DROP INDEX public."proyectos_proyecto_Grupo_trabajo_f543c3f9";
       public         root    false    188    2191            �           1259    40689 /   proyectos_proyecto_Nombre_5aa85695e8c06938_like    INDEX     �   CREATE INDEX "proyectos_proyecto_Nombre_5aa85695e8c06938_like" ON proyectos_proyecto USING btree ("Nombre" varchar_pattern_ops);
 E   DROP INDEX public."proyectos_proyecto_Nombre_5aa85695e8c06938_like";
       public         root    false    186    2191            �           1259    40688    proyectos_proyecto_f4cd2b0a    INDEX     `   CREATE INDEX proyectos_proyecto_f4cd2b0a ON proyectos_proyecto USING btree ("Scrum_Master_id");
 /   DROP INDEX public.proyectos_proyecto_f4cd2b0a;
       public         root    false    186    2191            �           1259    40797    sprint_sprint_56ac0855    INDEX     Y   CREATE INDEX sprint_sprint_56ac0855 ON sprint_sprint USING btree ("Usuario_creador_id");
 *   DROP INDEX public.sprint_sprint_56ac0855;
       public         root    false    193    2191            �           1259    40843    sprint_sprint_80b83c89    INDEX     [   CREATE INDEX sprint_sprint_80b83c89 ON sprint_sprint USING btree ("Proyecto_asignado_id");
 *   DROP INDEX public.sprint_sprint_80b83c89;
       public         root    false    193    2191            �           1259    40798 *   sprint_sprint_Nombre_427388f816e1b2ae_like    INDEX     w   CREATE INDEX "sprint_sprint_Nombre_427388f816e1b2ae_like" ON sprint_sprint USING btree ("Nombre" varchar_pattern_ops);
 @   DROP INDEX public."sprint_sprint_Nombre_427388f816e1b2ae_like";
       public         root    false    193    2191            �           1259    40842 !   sprint_sprint_UserStorys_4d4c3b6a    INDEX     k   CREATE INDEX "sprint_sprint_UserStorys_4d4c3b6a" ON "sprint_sprint_UserStorys" USING btree (userstory_id);
 7   DROP INDEX public."sprint_sprint_UserStorys_4d4c3b6a";
       public         root    false    195    2191            �           1259    40841 !   sprint_sprint_UserStorys_b688f27b    INDEX     h   CREATE INDEX "sprint_sprint_UserStorys_b688f27b" ON "sprint_sprint_UserStorys" USING btree (sprint_id);
 7   DROP INDEX public."sprint_sprint_UserStorys_b688f27b";
       public         root    false    195    2191            �           1259    40903    userstory_cargarhoras_354ea2ca    INDEX     e   CREATE INDEX userstory_cargarhoras_354ea2ca ON userstory_cargarhoras USING btree ("US_asignado_id");
 2   DROP INDEX public.userstory_cargarhoras_354ea2ca;
       public         root    false    197    2191            �           1259    40776    userstory_userstory_5622a7cc    INDEX     f   CREATE INDEX userstory_userstory_5622a7cc ON userstory_userstory USING btree ("Usuario_asignado_id");
 0   DROP INDEX public.userstory_userstory_5622a7cc;
       public         root    false    191    2191            �           1259    40777    userstory_userstory_56ac0855    INDEX     e   CREATE INDEX userstory_userstory_56ac0855 ON userstory_userstory USING btree ("Usuario_creador_id");
 0   DROP INDEX public.userstory_userstory_56ac0855;
       public         root    false    191    2191            �           1259    40849    userstory_userstory_80b83c89    INDEX     g   CREATE INDEX userstory_userstory_80b83c89 ON userstory_userstory USING btree ("Proyecto_asignado_id");
 0   DROP INDEX public.userstory_userstory_80b83c89;
       public         root    false    191    2191            �           1259    40778 0   userstory_userstory_Nombre_7484bc344fd54706_like    INDEX     �   CREATE INDEX "userstory_userstory_Nombre_7484bc344fd54706_like" ON userstory_userstory USING btree ("Nombre" varchar_pattern_ops);
 F   DROP INDEX public."userstory_userstory_Nombre_7484bc344fd54706_like";
       public         root    false    191    2191            �           2606    40850 >   Proyecto_asignado_id_2695d2b245a67991_fk_proyectos_proyecto_id    FK CONSTRAINT     �   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT "Proyecto_asignado_id_2695d2b245a67991_fk_proyectos_proyecto_id" FOREIGN KEY ("Proyecto_asignado_id") REFERENCES proyectos_proyecto(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT "Proyecto_asignado_id_2695d2b245a67991_fk_proyectos_proyecto_id";
       public       root    false    186    191    1991    2191                        2606    40844 >   Proyecto_asignado_id_4faf80a0d82ce869_fk_proyectos_proyecto_id    FK CONSTRAINT     �   ALTER TABLE ONLY sprint_sprint
    ADD CONSTRAINT "Proyecto_asignado_id_4faf80a0d82ce869_fk_proyectos_proyecto_id" FOREIGN KEY ("Proyecto_asignado_id") REFERENCES proyectos_proyecto(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.sprint_sprint DROP CONSTRAINT "Proyecto_asignado_id_4faf80a0d82ce869_fk_proyectos_proyecto_id";
       public       root    false    193    1991    186    2191            �           2606    40486 ?   auth_content_type_id_508cf46651277a81_fk_django_content_type_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id;
       public       root    false    1931    166    164    2191            �           2606    40572 6   auth_group_Usuario_id_63c754eb6bfcbf97_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT "auth_group_Usuario_id_63c754eb6bfcbf97_fk_auth_user_id" FOREIGN KEY ("Usuario_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 m   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT "auth_group_Usuario_id_63c754eb6bfcbf97_fk_auth_user_id";
       public       root    false    1950    172    168    2191            �           2606    40493 ?   auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id;
       public       root    false    1942    170    168    2191            �           2606    40498 ?   auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id;
       public       root    false    170    166    1936    2191            �           2606    40523 ?   auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id;
       public       root    false    1936    176    166    2191            �           2606    40511 ;   auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id;
       public       root    false    1942    168    174    2191            �           2606    40506 9   auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id;
       public       root    false    174    1950    172    2191            �           2606    40518 ?   auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id;
       public       root    false    172    176    1950    2191            �           2606    40542 ?   djan_content_type_id_697914295151027a_fk_django_content_type_id    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id;
       public       root    false    178    1931    164    2191            �           2606    40547 9   django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id;
       public       root    false    178    1950    172    2191            �           2606    40650 ?   flujos_flu_actividad_id_59b690fd57c2646c_fk_flujos_actividad_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_flujo_Actividades"
    ADD CONSTRAINT flujos_flu_actividad_id_59b690fd57c2646c_fk_flujos_actividad_id FOREIGN KEY (actividad_id) REFERENCES flujos_actividad(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_flujo_Actividades" DROP CONSTRAINT flujos_flu_actividad_id_59b690fd57c2646c_fk_flujos_actividad_id;
       public       root    false    184    180    1972    2191            �           2606    40611 ?   flujos_fluj_Usuario_creador_id_66a0c65a8ec3a8fe_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY flujos_flujo
    ADD CONSTRAINT "flujos_fluj_Usuario_creador_id_66a0c65a8ec3a8fe_fk_auth_user_id" FOREIGN KEY ("Usuario_creador_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.flujos_flujo DROP CONSTRAINT "flujos_fluj_Usuario_creador_id_66a0c65a8ec3a8fe_fk_auth_user_id";
       public       root    false    182    172    1950    2191            �           2606    40655 ?   flujos_flujo_Activ_flujo_id_3db7e564f60f262d_fk_flujos_flujo_id    FK CONSTRAINT     �   ALTER TABLE ONLY "flujos_flujo_Actividades"
    ADD CONSTRAINT "flujos_flujo_Activ_flujo_id_3db7e564f60f262d_fk_flujos_flujo_id" FOREIGN KEY (flujo_id) REFERENCES flujos_flujo(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."flujos_flujo_Actividades" DROP CONSTRAINT "flujos_flujo_Activ_flujo_id_3db7e564f60f262d_fk_flujos_flujo_id";
       public       root    false    184    182    1978    2191            �           2606    40708 ?   proyectos_p_Usuario_creador_id_38d44a92317cc7c4_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY proyectos_proyecto
    ADD CONSTRAINT "proyectos_p_Usuario_creador_id_38d44a92317cc7c4_fk_auth_user_id" FOREIGN KEY ("Usuario_creador_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.proyectos_proyecto DROP CONSTRAINT "proyectos_p_Usuario_creador_id_38d44a92317cc7c4_fk_auth_user_id";
       public       root    false    186    172    1950    2191            �           2606    40723 ?   proyectos_proy_Scrum_Master_id_144dc0737423a5d7_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY proyectos_proyecto
    ADD CONSTRAINT "proyectos_proy_Scrum_Master_id_144dc0737423a5d7_fk_auth_user_id" FOREIGN KEY ("Scrum_Master_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.proyectos_proyecto DROP CONSTRAINT "proyectos_proy_Scrum_Master_id_144dc0737423a5d7_fk_auth_user_id";
       public       root    false    172    186    1950    2191            �           2606    40713 ?   proyectos_proyecto_Gru_user_id_44d9f00ab5a73817_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo"
    ADD CONSTRAINT "proyectos_proyecto_Gru_user_id_44d9f00ab5a73817_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."proyectos_proyecto_Grupo_trabajo" DROP CONSTRAINT "proyectos_proyecto_Gru_user_id_44d9f00ab5a73817_fk_auth_user_id";
       public       root    false    188    172    1950    2191            �           2606    40718 ?   proyectos_proyecto_id_190ad33de9827525_fk_proyectos_proyecto_id    FK CONSTRAINT     �   ALTER TABLE ONLY "proyectos_proyecto_Grupo_trabajo"
    ADD CONSTRAINT proyectos_proyecto_id_190ad33de9827525_fk_proyectos_proyecto_id FOREIGN KEY (proyecto_id) REFERENCES proyectos_proyecto(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."proyectos_proyecto_Grupo_trabajo" DROP CONSTRAINT proyectos_proyecto_id_190ad33de9827525_fk_proyectos_proyecto_id;
       public       root    false    188    1991    186    2191                       2606    40836 ?   sprint__userstory_id_1bfe27b6ad70d8e6_fk_userstory_userstory_id    FK CONSTRAINT     �   ALTER TABLE ONLY "sprint_sprint_UserStorys"
    ADD CONSTRAINT sprint__userstory_id_1bfe27b6ad70d8e6_fk_userstory_userstory_id FOREIGN KEY (userstory_id) REFERENCES userstory_userstory(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."sprint_sprint_UserStorys" DROP CONSTRAINT sprint__userstory_id_1bfe27b6ad70d8e6_fk_userstory_userstory_id;
       public       root    false    195    191    2009    2191            �           2606    40792 ?   sprint_spri_Usuario_creador_id_75cf8853232a8ac6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY sprint_sprint
    ADD CONSTRAINT "sprint_spri_Usuario_creador_id_75cf8853232a8ac6_fk_auth_user_id" FOREIGN KEY ("Usuario_creador_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.sprint_sprint DROP CONSTRAINT "sprint_spri_Usuario_creador_id_75cf8853232a8ac6_fk_auth_user_id";
       public       root    false    172    193    1950    2191                       2606    40831 ?   sprint_sprint_Us_sprint_id_1f59335fd4aa3ee1_fk_sprint_sprint_id    FK CONSTRAINT     �   ALTER TABLE ONLY "sprint_sprint_UserStorys"
    ADD CONSTRAINT "sprint_sprint_Us_sprint_id_1f59335fd4aa3ee1_fk_sprint_sprint_id" FOREIGN KEY (sprint_id) REFERENCES sprint_sprint(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."sprint_sprint_UserStorys" DROP CONSTRAINT "sprint_sprint_Us_sprint_id_1f59335fd4aa3ee1_fk_sprint_sprint_id";
       public       root    false    193    195    2016    2191                       2606    40898 ?   users_US_asignado_id_440aa667ed2f46e9_fk_userstory_userstory_id    FK CONSTRAINT     �   ALTER TABLE ONLY userstory_cargarhoras
    ADD CONSTRAINT "users_US_asignado_id_440aa667ed2f46e9_fk_userstory_userstory_id" FOREIGN KEY ("US_asignado_id") REFERENCES userstory_userstory(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.userstory_cargarhoras DROP CONSTRAINT "users_US_asignado_id_440aa667ed2f46e9_fk_userstory_userstory_id";
       public       root    false    191    2009    197    2191            �           2606    40766 ?   userstory__Usuario_asignado_id_6b3174574270adab_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT "userstory__Usuario_asignado_id_6b3174574270adab_fk_auth_user_id" FOREIGN KEY ("Usuario_asignado_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT "userstory__Usuario_asignado_id_6b3174574270adab_fk_auth_user_id";
       public       root    false    172    191    1950    2191            �           2606    40771 ?   userstory_us_Usuario_creador_id_5747c880a471a6e_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY userstory_userstory
    ADD CONSTRAINT "userstory_us_Usuario_creador_id_5747c880a471a6e_fk_auth_user_id" FOREIGN KEY ("Usuario_creador_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.userstory_userstory DROP CONSTRAINT "userstory_us_Usuario_creador_id_5747c880a471a6e_fk_auth_user_id";
       public       root    false    172    191    1950    2191            p   4   x�3��M,.I-�4204�50�56P02�26�24�33732�rr��qqq �	b      r   �   x�л�0�X*����v/�U4L�@P�KK[Y4hӤC�޴�C���ު�>���Ұs1�,
�L
�l
��
��
��
��
��-r[�>�"��@nˁܖ�-r[��c9��r"��Dˉ<�������)�      n   �  x�]�Kn� @��9A5@��^�R������d*��1Lvؼ�Pl#ŻY+3M��͕]�R���c
��۬�-��ʠFp�w{�`He�N����e��
�֜��{�Čm��`���.�g���(�5���I���"A�@�[<v�E�翖 %?�v�� (~<tz t:|t�q���xnV4(��+��L΂o����
�M7�m��-^�"��@fȝ��{3Fʄ�i�{��p�-C!�[�1����@Y�Kc�$P%���o��$z����ZΑ��5s��m�����qb@-�A�\�IGH�U!!}����g�b15LH,`����_�b����PT��^O�L��	��: �dsB��K�����������y�ޝ������qt���s� ���� ����&      t   �  x�}�]o�@���_�w'ŝe�&=E�Z�%�~�I�"ࢀ�ê����i�&��7��;O^�g�yB^� �P�a������Ɩ������e�2�\�k�>�=�S�S�Y��h�M����3b� �D�	h�2�2�-J�\l��=,kqZ\���+-*���41&Й'@-z0AH'��|]���/���^����M�xN��yw'Y��a9��J��K���E�|L�#'`�M�F����i��<�E����	1���Q!��ɩ�#�%T~|��)�j��9�:s޼G�\�-�ԩ�����L�:H�����q�ɨ�^�
c��MJ�)]Ym�,N}�G�{�`�8�~O����������X�5��"m��Xʋ�(����      v      x�3�4�4����� �Y      x      x������ � �      z      x������ � �      l   �   x�]�K� ��)r���߻t�M�@����7@�]�yc�
��5�M�����K�DK�cv��N�o:���b���-U�	�`����F�h����/��n�&/�W�&k$��+���v�n�9��<[ޫZ%P�#9/��J�'7,a����� FS���iޜ��X|���=y      j   �  x����n�0@��W�yn��-+Ylʶ���Կ��4����(�r3���q8��i�?��Tc ��~�۷
ȓ�'t��4�5(�E����V�e~�G�Z�LU��{��x4�vAx{F}7���P���jC�9^`�`�c�>|t�2uc���G{�S�mz���
�҂��]���a� �7�f0)l|b��a��5�q��5�K;�C�$�V	���@�,�
B����o��E�&�aH��}�Lǡȳ#��x��D$S:i��j���|[)�R�i�kҲ�T:P�G}i�$�V�q����s5ü��r.;:MDMPT��K
>7�Ob�rjS��(�
� �1�B~(�T�P� :�I�"�B�D��`�%U1W�x��)�ǹ�芊e`W��EV#��P����&�0�B1o-bjd��eCM�0~��@������j:��i�1�������+T]y1��|+��c\�SQ���$C�ق@�1�odv���m)�X_5��+�ռ���S�\؜j!a#Y0φwi<�e�zj�G$׈�/c��Bi@j��c�9Dv���74�6���7~��] �@�Fh6F�����mA~�f�����AUH�u��ZR�+ܭ"�UTA��߆<q���A}<��K;�c;�Y4���뿎���p��(b�      �   
  x���͎�0F��S���4�4@
��y ��!a�d�0?����V��UՅ��+[����`���m�"D�ꍼ����U�؞0D{���ykL��K41���EE5T�J�K~2��P���[�*���=N��Ge�L�	�PE�r<L	���D�u�n�{�%h��Z�$���m�R�S�.<���GQ%Э=褎��u�I�t�]�5���|�w��g�k�ܦ�D*Gi'7���9GV�w� $s@��\aw��h<��]s�r����|�9]&�)�?t9%B5�P3��%�ꘇ�̢1���� LG�Pk#�o��GṱL��~����Vx�  �<�K��ݾ�VvQ�So[�r��.*t��O�$΂��d�j��~�SE-�"�xd�V�7�fF{ڿK~셩*���l�P��Y����05��!�^c�,��}{QC���܆�{1��gg�oά�+W ,\ڎ�ȭ����Ɵ�nǲ!������qj��w��Ù������b:�~ j��      |   $   x�3�L4�B.#�D#N# Ø3ј�Ȉ���� OW�      ~   ?   x�3��,1�tL.�,��,/N+NI�4204�50�52W04�26�26�31460
rq��qqq ���      �      x�3�4�4�2�F\�@Ҙ+F��� !��      �   d   x�}�=� @Ṝ�@�R��!`SH��W��f�7|�g[�К����mo}6 `$oPGM��2��R��+�	�$͔�e��$�@�J��f?      �   '   x���4�4�24 RF\��@ʘ�H�x�@ʘ+F��� eD�      �   �   x�}�;
�0�zu
_�bw��>���.�A�'��4��Dz}�[m�X���1B�R�[��X��=2qʐ̰���ȍ�f�N	4�O��:+11�EZ}�'�8�e����c�t��	�p��<g�6����Y�1�=B�      �   .   x���  �7��x�b�u�6�X��*x#�|��$~5�      �   :   x�34�44�t�I�W�Ȭ��46�24�4��KLIs�9-9=�2
�y
��`1z\\\ �|�      �     x���Aj�0��������d������&ĢxQ;������1Q������若�%Χu���P���#�_�y�c?�q���6i�`���-Km,	q�J�PATNj�.�,��x��m�ucm�^����η�w�&�~�
�s��]k}fQ�M�:��s��-0�OLW��r>�bt�tO`.`��c�3�:�g��^�p��.@�EM�|Q}\��p�ӑn� �� �O��J���	����m�������������     